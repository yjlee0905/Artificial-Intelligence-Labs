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

    def setRewards(self):
        for key in self.nodes:
            if key in self.rewards:
                self.rewards[key] = float(self.rewards[key])
            else:
                self.rewards[key] = 0.0


    def setAndValidateTerminals(self):
        for node in self.nodes:
            if node not in self.edges:
                self.terminals.append(node)

    def parseAndValidateProbabilites(self):

        # convert to number in chance nodes
        for key in self.chanceNodes:
            probabilities = self.chanceNodes[key]
            for i in range(0, len(probabilities)):
                if probabilities[i].count('.') == 1:
                    chanceNode = probabilities[i]
                    idx = chanceNode.find('.')
                    numerator = chanceNode[idx + 1:].strip()
                    denominator = pow(10, len(numerator))
                    decimal = float(numerator) / denominator
                    probabilities[i] = decimal
                elif probabilities[i].strip() == '1':
                    probabilities[i] = float(probabilities[i])
                else:
                    print probabilities[i] + ' has wrong format of probability'
                    # TODO exit?
            self.chanceNodes[key] = probabilities

        # validate chance nodes
        for node in self.chanceNodes:
            if len(self.edges[node]) != len(self.chanceNodes[node]):
                print 'Node ' + node + ' does not have the same number of edges and probabilities.'

            sum = 0.0
            for i in range(0, len(self.chanceNodes[node])):
                sum += self.chanceNodes[node][i]
            if sum != 1.0:
                print 'The probability of node ' + node + ' does not add up to 1.'
                exit()

        # convert to number in decision nodes
        for key in self.decisionNodes:
            if self.decisionNodes[key].count('.') == 1:
                decisionNode = self.decisionNodes[key]
                idx = decisionNode.find('.')
                numerator = decisionNode[idx + 1:].strip()
                denominator = pow(10, len(numerator))
                decimal = float(numerator) / denominator
                self.decisionNodes[key] = decimal
            elif self.decisionNodes[key].strip() == '1':
                self.decisionNodes[key] = float(self.decisionNodes[key])
            else:
                print key + ' has wrong format of probability'
                # TODO exit?

        for node in self.edges:
            if node not in self.decisionNodes and node not in self.chanceNodes:
                self.decisionNodes[node] = 1.0