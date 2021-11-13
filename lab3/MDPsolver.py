from Parser import Parser
import sys


class MDPsolver(Parser):

    def __init__(self, parser, df, tol, iter, min):
        # Parser.__init__(self)
        self.chanceNodes = parser.chanceNodes
        self.decisionNodes = parser.decisionNodes
        self.rewards = parser.rewards
        self.edges = parser.edges
        self.nodes = parser.nodes
        self.terminals = parser.terminals

        self.df = df
        self.tol = tol
        self.iter = iter
        self.min = min


    def runMDP(self):
        # set initial policy TODO check initial policy
        policy = {}
        for key in self.edges:
            #if key in self.decisionNodes:
            policy[key] = self.edges[key][0]

        while True:
            values = self.valueIteration(policy)
            newPolicy = self.policyIteration(values)
            print values
            print newPolicy
            if self.isPolicySame(policy, newPolicy):
                break
            policy = newPolicy

        # print Result
        for node in policy:
            print node + ' -> ' + policy[node]
        for node in values:
            print node + '=' + "{:.3f}".format(values[node]),


    def isPolicySame(self, prevPolicy, newPolicy):
        for node in prevPolicy:
            if prevPolicy[node] != newPolicy[node]:
                return False
        return True

    def valueIteration(self, policy):
        # initialize rewards
        prevRewards = {}
        for node in self.rewards:
            prevRewards[node] = self.rewards[node]
        curRewards = {}

        idx = 0
        maxDiff = sys.float_info.max
        while idx < self.iter and maxDiff > self.tol: # TODO check tol
            for node in self.nodes:
                value = self.rewards[node]

                if node in self.decisionNodes:
                    prob = self.decisionNodes[node]
                    rest = 0.0
                    if self.decisionNodes[node] != 1.0:
                        rest = (1 - self.decisionNodes[node]) / (len(self.edges[node]) - 1)

                    for nextNode in self.edges[node]:
                        if policy[node] == nextNode:
                            value += self.df * prob * prevRewards[nextNode]
                        else:
                            value += self.df * rest * prevRewards[nextNode]

                elif node in self.chanceNodes:
                    for i in range(0, len(self.edges[node])):
                        prob = self.chanceNodes[node][i]
                        nextNode = self.edges[node][i]
                        value += self.df * prob * prevRewards[nextNode]

                elif node in self.edges and len(self.edges[node]) == 1: # TODO change to single detination
                    nextNode = self.edges[node][0]
                    value += prevRewards[nextNode]

                curRewards[node] = value

            diff = 0.0
            for node in curRewards:
                if abs(curRewards[node] - prevRewards[node]) > diff:
                    diff = abs(curRewards[node] - prevRewards[node])
            maxDiff = diff
            idx += 1

            for node in curRewards:
                prevRewards[node] = curRewards[node]

        return prevRewards


    def policyIteration(self, values):
        newPolicy = {}

        if self.min:
            for node in self.nodes:
                if node not in self.edges:
                    # TODO check what if no next node
                    newPolicy[node] = node
                else:
                    nextNodes = self.edges[node]
                    minValue = sys.float_info.max
                    minNode = node
                    for nextNode in nextNodes:
                        if minValue > values[nextNode]:
                            minValue = values[nextNode]
                            minNode = nextNode
                    newPolicy[node] = minNode

        else:
            for node in self.nodes:
                if node not in self.edges:
                    newPolicy[node] = node
                else:
                    nextNodes = self.edges[node]
                    maxValue = sys.float_info.min
                    maxNode = node
                    for nextNode in nextNodes:
                        if maxValue < values[nextNode]:
                            maxValue = values[nextNode]
                            maxNode = nextNode
                    newPolicy[node] = maxNode

        return newPolicy