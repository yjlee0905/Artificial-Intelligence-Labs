import Constant
import argparse
from Parser import Parser
from DPLLsolver import DPLLsolver
from BNFtoCNFconverter import BNFtoCNFconverter

def runCNFconverter(fileName, isVerbose, isSolverMode):
    parser = Parser()
    sentences = parser.parseAndFormatSentences(fileName)

    converted = []
    for sentence in sentences:

        parser = Parser()
        parseTree = parser.parse(sentence, Constant.OPERATORS)

        converter = BNFtoCNFconverter()
        step1 = converter.eliminateIff(parseTree)
        if isVerbose:
            print("step1: Eliminate <=> (If and Only If)")
            converter.printStepResult(step1)

        step2 = converter.eliminateImplication(step1)
        if isVerbose:
            print("step2: Eliminate => (Implication)")
            step2Res = []
            converter.printStep2Result(step2, step2Res)
            for i in range(0, len(step2Res)):
                print(step2Res[i] + ' ', end='')
            print()

        step3 = converter.applyDeMorganLaw(step2)
        if isVerbose:
            print("step3: Apply DeMorgan's Law")
            converter.printStepResult(step3)

        step4 = converter.applyDistributiveLaw(step3)
        if isVerbose:
            print("step4: Apply Distributive Law")
            converter.printStepResult(step4)

        resultStep5 = converter.separateSentences(step4)
        if isVerbose:
            print("step5: Separate Sentences")
            for res in resultStep5:
                print(res)

        elif not isSolverMode:
            for res in resultStep5:
                print(res)

        converted += resultStep5

    return converted


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', type=str, default='solver', help="Mode: cnf, dpll, solver")
    parser.add_argument('-v', type=bool, default=False, help="Default: False, Support verbose mode for True")
    parser.add_argument('-file', type=str, help="Please specify input file name.")

    args = parser.parse_args()
    mode = args.mode
    fileName = args.file
    isVerbose = args.v

    if fileName is None:
        print("Please specify your input file.")
        exit()

    if mode == 'dpll':
        # fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2/inputs/dpexample4.txt'

        parsedSentences = []
        sentences = open(fileName, 'r').read().split('\n')
        for sentence in sentences:
            parsed = sentence.split(' ')
            parsedSentences.append(parsed)

        dpllSolver = DPLLsolver()
        atoms = dpllSolver.parseAtoms(sentences=parsedSentences)
        result = dpllSolver.runDPLL(atoms, parsedSentences, isVerbose)

        if result[Constant.RESULT] == Constant.FAILURE:
            print("NO VALID ASSIGNMENT")
        elif result[Constant.RESULT] == Constant.SUCCESS:
            for key in result:
                if key is not Constant.RESULT:
                    print(key + " = " + result[key])

    elif mode == 'cnf':
        # fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2/inputs/example1.txt'
        runCNFconverter(fileName, isVerbose, False)

    elif mode == 'solver':
        # fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2/inputs/example2.txt'
        cnfFormed = runCNFconverter(fileName, isVerbose, True)

        converted = []
        for cnfSentence in cnfFormed:
            converted.append(cnfSentence.split())

        if isVerbose:
            print("Run DPLL algorithm")
        dpllSolver = DPLLsolver()
        atoms = dpllSolver.parseAtoms(converted)
        result = dpllSolver.runDPLL(atoms, converted, isVerbose)

        if result[Constant.RESULT] == Constant.FAILURE:
            print("NO VALID ASSIGNMENT")
        elif result[Constant.RESULT] == Constant.SUCCESS:
            for key in result:
                if key is not Constant.RESULT:
                    print(key + " = " + result[key])