from Parser import Parser
from MDPsolver import MDPsolver
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-df', type=float, default=1.0)
    parser.add_argument('-min', type=bool, default=False)
    parser.add_argument('-tol', type=float, default=0.001)
    parser.add_argument('-iter', type=int, default=100)
    parser.add_argument('-file', type=str)

    args = parser.parse_args()
    df = 0.9
    isMin = False
    tol = 0.001
    iter = 100
    fileName = args.file

    # if fileName is None:
    #     print "Please specify your input file."
    #     exit()

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab3/inputs/teach.txt'

    parser = Parser()
    parser.parse(fileName)

    solver = MDPsolver(parser, df, tol, iter, isMin)
    solver.runMDP()