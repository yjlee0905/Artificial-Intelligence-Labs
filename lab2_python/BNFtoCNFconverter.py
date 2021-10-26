import re
import Constant

class Binary:
    def __init__(self, op, sign, token1, token2):
        self.op = op
        self.sign = sign
        self.left = token1
        self.right = token2

    def inorderTraversal(self, root, answer):
        if isinstance(root, Binary) is False:
            answer.append(root)
            return

        self.inorderTraversal(root.left, answer)
        answer.append(root.op)
        self.inorderTraversal(root.right, answer)
        return


class BNFtoCNFconverter:

    def parse(self, sentence, op):
        if not op:
            sentence = sentence.strip()
            if sentence[0] == '!':
                sentence = sentence.replace(' ', '')
            return sentence
        idx = sentence.rfind(op[0])
        if idx == -1:
            sentence = sentence.strip()
            if sentence[0] == '!':
                sentence = sentence.replace(' ', '')
            return self.parse(sentence, op[1:])
        return Binary(op[0], True, self.parse(sentence[:idx], op), self.parse(sentence[idx+len(op[0]):], op))


    def eliminateIff(self, node):
        if type(node) == str:
            return node

        left = self.eliminateIff(node.left)
        right = self.eliminateIff(node.right)

        if node.op != "<=>":
            return Binary(node.op, node.sign, left, right)

        return Binary("&", True, Binary("=>", True, left, right), Binary("=>", True, right, left))


    def eliminateImplication(self, node):
        if type(node) == str:
            return node

        left = self.eliminateImplication(node.left)
        right = self.eliminateImplication(node.right)

        if node.op != "=>":
            return Binary(node.op, node.sign, left, right)

        # TODO change left sign
        # left = Binary("|", not node.sign, left, right)
        if type(left) == str:
            left = '!' + left
        else:
            left.sign = not left.sign
        # if type(left) != str:
        #     left.sign = not left.sign
        return Binary("|", node.sign, left, right)


    def applyDeMorganLaw(self, node):
        if type(node) == str:
            return node

        left = self.applyDeMorganLaw(node.left)
        right = self.applyDeMorganLaw(node.right)

        if node.sign is True:
            return Binary(node.op, node.sign, left, right)

        if node.op == '&':
            node.op = '|'
        elif node.op == '|':
            node.op = '&'

        if type(left) != str:
            left.sign = not left.sign
            left = self.applyDeMorganLaw(left)
        else:
            if left[0] == '!':
                left = left[1:]
            else:
                left = '!' + left

        if type(right) != str:
            right.sign = not right.sign
            right = self.applyDeMorganLaw(right)
        else:
            if right[0] == '!':
                right = right[1:]
            else:
                right = '!' + right

        return Binary(node.op, not node.sign, left, right)


    def applyDistributiveLaw(self, node):
        if type(node) == str:
            return node

        node.left = self.applyDistributiveLaw(node.left)
        node.right = self.applyDistributiveLaw(node.right)
        # TODO &

        if node.op == '|':
            if type(node.left) != str and node.left.op == '&':
                # TODO overwriting  P <=> Q <=> R check
                # TODO new node, X overwrite
                # make left child  (A|C)
                # make right child  (B|C)
                newLeft = Binary('|', node.sign, node.left.left, node.right)
                newRight = Binary('|', node.sign, node.left.right, node.right)
                node.op = '&'

                node.left = self.applyDistributiveLaw(newLeft)
                node.right = self.applyDistributiveLaw(newRight)

            elif type(node.right) != str and node.right.op == '&':
                # make left child  (A|C)
                # make right child  (B|C)
                newLeft = Binary('|', node.sign, node.right.left, node.left)
                newRight = Binary('|', node.sign, node.right.right, node.left)
                node.op = '&'

                node.left = self.applyDistributiveLaw(newLeft)
                node.right = self.applyDistributiveLaw(newRight)

        return Binary(node.op, node.sign, node.left, node.right)


    def separateSentences(self, node):
        separated = []
        node.inorderTraversal(node, separated)

        result = []
        strSeparated = ''
        for atom in separated:
            if atom == '|':
                continue
            elif atom == '&':
                strSeparated = strSeparated.strip()
                result.append(strSeparated)
                strSeparated = ''
            else:
                strSeparated += (atom + ' ')

        if len(strSeparated) > 0:
            strSeparated = strSeparated.strip()
            result.append(strSeparated)

        return result