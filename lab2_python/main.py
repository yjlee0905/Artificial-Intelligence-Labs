import Constant
from Parser import Parser
from DPLLsolver import DPLLsolver
#from BNFtoCNFconverter import BNFtoCNFconverter
from Converter import BNFtoCNFconverter

def printCNF(results):
    for result in results:
        line = result.split(' & ')
        for clause in line:
            if clause[0] == '(' and clause[-1] == ')':
                clause = clause[1:-1]
            clause = formatResult(clause)
            print clause


def formatResult(line):
    newLine = ''
    idx = 0
    while idx < len(line):
        if line[idx] == '!':
            newLine += line[idx]
            idx += 1
        elif line[idx] == '|':
            idx += 1
            continue
        else:
            newLine += line[idx]
        idx += 1
    return newLine


if __name__ == "__main__":

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/example1.txt'
    parser = Parser()
    sentences = parser.parseAndFormatSentences(fileName)

    for sentence in sentences:
        converter = BNFtoCNFconverter(sentence)
        printCNF(converter.runConverter(sentence))

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






