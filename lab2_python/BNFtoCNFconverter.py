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
            print root
            answer.append(root)
            return

        self.inorderTraversal(root.left, answer)
        answer.append(root.op)
        self.inorderTraversal(root.right, answer)
        return

    def isAtom(self):
        if self.left is None and self.right is None:
            return True
        return False



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
        return Binary(op[0], False, self.parse(sentence[:idx], op), self.parse(sentence[idx+len(op[0]):], op))


    def eliminateIff(self, node):
        if type(node) == str:
            return node

        left = self.eliminateIff(node.left)
        right = self.eliminateIff(node.right)

        if node.op != "<=>":
            return Binary(node.op, node.sign, left, right)

        return Binary("&", True, Binary("=>", True, left, right), Binary("=>", True, right, left))

