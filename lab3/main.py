from Parser import Parser
from MDPsolver import MDPsolver

if __name__ == "__main__":
    print('start lab3')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab3/inputs/maze.txt'

    parser = Parser()
    parser.parse(fileName)

    #solver = MDPsolver(parser.chanceNodes, parser.decisionNodes, parser.rewards, parser.edges, parser.nodes, parser.terminals)
    solver = MDPsolver(parser, 1.0, 0.001, 50, False)
    solver.runMDP()




