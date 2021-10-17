from DPLLsolver import DPLLsolver

if __name__ == "__main__":
    print('start lab2')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/dpexample3.txt'
    sentences = open(fileName, 'r').read().split('\n')
    print(sentences)

    parsedSentences = []
    for sentence in sentences:
        parsed = sentence.split(' ')
        parsedSentences.append(parsed)

    d = DPLLsolver()
    a = d.parseAtoms(sentences=parsedSentences)
    print(d.findPureLiterals(sentences=parsedSentences, atoms=a))
    d.runDPLL(sentences=parsedSentences, atoms=a)




