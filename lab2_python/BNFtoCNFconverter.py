import re
import Constant

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
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
        return Binary(self.parse(sentence[:idx], op), op[0], self.parse(sentence[idx+len(op[0]):], op))
