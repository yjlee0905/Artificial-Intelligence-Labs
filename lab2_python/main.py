import Constant
from Parser import Parser
from DPLLsolver import DPLLsolver
#from BNFtoCNFconverter import BNFtoCNFconverter
from Converter import BNFtoCNFconverter

if __name__ == "__main__":
    print('start lab2')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/example1.txt'
    parser = Parser()
    sentences = parser.parseAndFormatSentences(fileName)

    for sentence in sentences:
        converter = BNFtoCNFconverter(sentence)
        converter.runConverter(sentence)

    # for sentence in sentences:
    #     converter = BNFtoCNFconverter(sentence)
    #
    #     tree = converter.parse(sentence, Constant.OPERATORS)
    #     result = []
    #     tree.inorderTraversal(tree, result)
    #     print(result)


    # parsedSentences = []
    # for sentence in sentences:
    #     parsed = sentence.split(' ')
    #     parsedSentences.append(parsed)

    # d = DPLLsolver()
    # a = d.parseAtoms(sentences=parsedSentences)
    # print(d.findPureLiterals(sentences=parsedSentences, atoms=a))
    # result = d.runDPLL(sentences=parsedSentences, atoms=a)
    # for key in result:
    #     if key is not Constant.RESULT:
    #         print key + " = " + result[key]




