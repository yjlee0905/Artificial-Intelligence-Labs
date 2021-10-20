import Constant
from DPLLsolver import DPLLsolver
from BNFtoCNFconverter import BNFtoCNFconverter

if __name__ == "__main__":
    print('start lab2')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/dpexample4.txt'
    sentences = open(fileName, 'r').read().split('\n')
    print(sentences)

    converter = BNFtoCNFconverter()


    for sentence in sentences:
        converter.parse(sentence, Constant.OPERATORS)
        print("hello")



    parsedSentences = []
    for sentence in sentences:
        parsed = sentence.split(' ')
        parsedSentences.append(parsed)

    d = DPLLsolver()
    a = d.parseAtoms(sentences=parsedSentences)
    print(d.findPureLiterals(sentences=parsedSentences, atoms=a))
    print(d.runDPLL(sentences=parsedSentences, atoms=a))




