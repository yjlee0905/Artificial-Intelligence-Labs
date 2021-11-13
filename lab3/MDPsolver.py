from Parser import Parser


class MDPsolver(Parser):

    def __init__(self, parser):
        # Parser.__init__(self)
        self.chanceNodes = parser.chanceNodes
        self.decisionNodes = parser.decisionNodes
        self.rewards = parser.rewards
        self.edges = parser.edges
        self.nodes = parser.nodes
        self.terminals = parser.terminals


    def runMDP(self, iter, tol):
        # set initial policy
        policy = {}
        for key in self.edges:
            policy[key] = self.edges[key][0]
        print policy

        values = {}
        policies = {}
        for i in range(0, iter):
            print("here")
            # valueiteration
            # greedy policy computation


    def valueIteration(self, policy, iter, tol):
        # initialize rewards
        curRewards = {}
        for node in self.rewards:
            curRewards[node] = self.rewards[node]

        idx = 0
        while idx < iter: # TODO check tol
            for node in self.nodes:
                if node in self.decisionNodes:
                    print("TODO: decision node")
                elif node in self.chanceNodes:
                    for edge in self.edges:
                        print("TODO: chance node")
                elif node in self.terminals: # TODO change to single detination
                    print("TODO: terminal node")






