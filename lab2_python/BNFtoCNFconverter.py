import re
import Constant

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
        self.right = token2

    # def printTree(self):
    #     if self.left:
    #         self.left.printTree()
    #     print self.op
    #     if self.right:
    #         self.right.printTree()
    #
    # def inorderTraversal(self, root):
    #     res = []
    #     if root:
    #         print root.left
    #         res.append(root.op)
    #         res = res + self.inorderTraversal(root.right)
    #     return res



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

    # def parseInput(self, fileName):
    #     lines = open(fileName, 'r').read().split('\n')
    #
    #     for line in lines:
    #         iffOccur = line.find('<=>')
    #         implyOccur = line.find('=>')
    #         andOccur = line.find('&')
    #         orOccur = line.find('|')