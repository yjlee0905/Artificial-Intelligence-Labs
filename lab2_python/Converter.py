import re
import Constant

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
        self.right = token2

    def inorderTraversal(self, root, result):
        if isinstance(root, Binary) is False:
            print root
            result.append(root)
            return

        self.inorderTraversal(root.left, result)
        result.append(root.op)
        self.inorderTraversal(root.right, result)
        return



class BNFtoCNFconverter:

    def runConverter(self, fileName):
        sentences = open(fileName, 'r').read().split('\n')

        for sentence in sentences:
            parsed = []
            tree = self.parse(sentence, Constant.OPERATORS)
            tree.inorderTraversal(tree, parsed)
            print parsed


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
