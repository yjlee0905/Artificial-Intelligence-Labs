from Parser import Parser
from MDPsolver import MDPsolver

if __name__ == "__main__":
    print('start lab3')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab3/inputs/teach.txt'

    parser = Parser()
    parser.parse(fileName)

    #solver = MDPsolver(parser.chanceNodes, parser.decisionNodes, parser.rewards, parser.edges, parser.nodes, parser.terminals)
    solver = MDPsolver(parser)
    solver.runMDP(100, 0.01)




