import Constant
import argparse
from Parser import Parser
from DPLLsolver import DPLLsolver
from Converter import BNFtoCNFconverter

def makeInputForDPLL(results):
    inputs = []
    for result in results:
        line = result.split(' & ')
        for clause in line:
            if clause[0] == '(' and clause[-1] == ')':
                clause = clause[1:-1]
            clause = formatResult(clause)
            clause = clause.strip().split()
            inputs.append(clause)
    return inputs


def printCNF(results, isVerbose):
    if isVerbose:
        print "step5: Separate top-level conjunctions into separate sentences"

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
    isNegate = False
    while idx < len(line):
        if line[idx] == '!':
            newLine += line[idx]
            isNegate = True
            idx += 1
        elif line[idx] == '|':
            idx += 1
            continue
        elif isNegate and line[idx] == ' ':
            idx += 1
            continue
        elif isNegate and line[idx] != ' ':
            isNegate = False
            newLine += line[idx]
            idx += 1
        else:
            newLine += line[idx]
            idx += 1
    return newLine


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-mode', type=str)
    parser.add_argument('-v', type=bool, default=False)
    parser.add_argument('-file', type=str)

    args = parser.parse_args()
    mode = args.mode
    fileName = args.file
    isVerbose = args.v

    if mode == 'dpll':
        # DPLL solver
        # fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/dpexample4.txt'

        parsedSentences = []
        sentences = open(fileName, 'r').read().split('\n')
        for sentence in sentences:
            parsed = sentence.split(' ')
            parsedSentences.append(parsed)

        dpllSolver = DPLLsolver()
        atoms = dpllSolver.parseAtoms(sentences=parsedSentences)
        result = dpllSolver.runDPLL(atoms, parsedSentences, isVerbose)

        if result[Constant.RESULT] == Constant.FAILURE:
            print "NO VALID ASSIGNMENT"
        elif result[Constant.RESULT] == Constant.SUCCESS:
            for key in result:
                if key is not Constant.RESULT:
                    print key + " = " + result[key]

    elif mode == 'cnf':
        # BNF to CNF converter
        # fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/example2.txt'
        parser = Parser()
        sentences = parser.parseAndFormatSentences(fileName)

        for sentence in sentences:
            converter = BNFtoCNFconverter(sentence)
            printCNF(converter.runConverter(sentence, isVerbose), isVerbose)
            if isVerbose:
                print

    elif mode == 'solver':

        #fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab2_python/inputs/example1.txt'
        parser = Parser()
        sentences = parser.parseAndFormatSentences(fileName)

        inputs = []
        for sentence in sentences:
            converter = BNFtoCNFconverter(sentence)
            converted =  converter.runConverter(sentence, isVerbose)
            printCNF(converted, isVerbose)
            if isVerbose:
                print
            inputs += makeInputForDPLL(converted)

        if isVerbose:
            print
            print "Run DPLL algorithm"
        dpllSolver = DPLLsolver()
        atoms = dpllSolver.parseAtoms(sentences=inputs)
        result = dpllSolver.runDPLL(atoms, inputs, isVerbose)

        if result[Constant.RESULT] == Constant.FAILURE:
            print "NO VALID ASSIGNMENT"
        elif result[Constant.RESULT] == Constant.SUCCESS:
            for key in result:
                if key is not Constant.RESULT:
                    print key + " = " + result[key]