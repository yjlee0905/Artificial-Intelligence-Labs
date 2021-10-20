import re
import Constant

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
        self.right = token2

    def printTree(self):
        if self.left:
            self.left.printTree()
        print self.op
        if self.right:
            self.right.printTree()


class BNFtoCNFconverter:

    def parse(self, sentence, op):
        if not op:
            return sentence
        idx = sentence.rfind(op[0])
        if idx == -1:
            return self.parse(sentence, op[1:])
        return Binary(self.parse(sentence[:idx]), op[0], self.parse(sentence[idx+len(op[0]):]))

    # def parseInput(self, fileName):
    #     lines = open(fileName, 'r').read().split('\n')
    #
    #     for line in lines:
    #         iffOccur = line.find('<=>')
    #         implyOccur = line.find('=>')
    #         andOccur = line.find('&')
    #         orOccur = line.find('|')



