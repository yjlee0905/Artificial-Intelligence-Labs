class Parser:

    def __init__(self):
        self.chanceNodes = {}
        self.decisionNodes = {}
        self.rewards = {}
        self.edges = {}
        self.nodes = set()
        self.terminals = []

    def parse(self, fileName):
        lines = open(fileName, 'r').read().split('\n')

        for line in lines:
            if len(line) == 0 or line.startswith('#'):
                continue

            # probabilities
            if '%' in line: # chance nodes or decision nodes
                splited = line.split('%')
                key = splited[0].strip()
                value = splited[1].strip()
                splitedValues = value.split(' ')
                for i in range(0, len(splitedValues)):
                    splitedValues[i] = splitedValues[i].strip()

                # split probabilities
                if len(splitedValues) == 1:
                    self.decisionNodes[key] = splitedValues[0]
                else:
                    self.chanceNodes[key] = splitedValues
            elif '=' in line: # rewards
                splited = line.split('=')
                key = splited[0].strip()
                value = splited[1].strip()
                self.rewards[key] = value
            elif ':' in line:
                splited = line.split(':')
                key = splited[0].strip()
                value = splited[1].strip()
                self.nodes.add(key)

                value = value.replace('[', '')
                value = value.replace(']', '')
                splitedValues = value.split(',')
                for i in range(0, len(splitedValues)):
                    splitedValues[i] = splitedValues[i].strip()
                    self.nodes.add(splitedValues[i])
                self.edges[key] = splitedValues

        self.setRewards()
        self.setAndValidateTerminals()
        self.parseAndValidateProbabilites()
        print(lines)

    def setRewards(self):
        for key in self.edges.keys():
            if key not in self.rewards:
                self.rewards[key] = 0

    def setAndValidateTerminals(self):
        for node in self.nodes:
            if node not in self.edges:
                self.terminals.append(node)

    def parseAndValidateProbabilites(self):

        for key in self.chanceNodes:
            if self.chanceNodes[key].count('.') == 1:
                chanceNode = self.chanceNodes[key]
                idx = chanceNode.find('.')
                numerator = chanceNode[idx + 1:].strip()
                denominator = pow(10, len(numerator))
                decimal = int(numerator) / denominator
                self.chanceNodes[key] = decimal
            else:
                print self.chanceNodes[key] + ' has wrong format of probability'
                # TODO exit?

        for key in self.decisionNodes:
            if self.decisionNodes[key].count('.') == 1:
                decisionNode = self.decisionNodes[key]
                idx = decisionNode.find('.')
                numerator = decisionNode[idx + 1:].strip()
                denominator = pow(10, len(numerator))
                decimal = float(numerator) / denominator
                self.decisionNodes[key] = decimal
            else:
                print self.decisionNodes[key] + ' has wrong format of probability'

        print(self.decisionNodes)
        print(self.chanceNodes)