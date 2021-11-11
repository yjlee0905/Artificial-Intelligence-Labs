class Parser:

    def parse(self, fileName):
        chanceNodes = {}
        decisionNodes = {}
        rewards = {}
        edges = {}

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
                    decisionNodes[key] = splitedValues[0]
                else:
                    chanceNodes[key] = splitedValues
            elif '=' in line: # rewards
                splited = line.split('=')
                key = splited[0].strip()
                value = splited[1].strip()
                rewards[key] = value
            elif ':' in line:
                splited = line.split(':')
                key = splited[0].strip()
                value = splited[1].strip()

                value = value.replace('[', '')
                value = value.replace(']', '')
                splitedValues = value.split(',')
                for i in range(0, len(splitedValues)):
                    splitedValues[i] = splitedValues[i].strip()
                edges[key] = splitedValues

        print(lines)