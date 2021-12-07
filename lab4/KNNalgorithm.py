from DistanceCalculator import DistanceCalculator

class KNNalgorithm:

    def __init__(self):
        self.calculator = DistanceCalculator()
        # {[p1, p2]: label}
        self.train = []
        self.test = []
        self.labels = set()

        # Precision and Recall
        self.numGot = {}
        self.numWant = {}
        self.numEquals = {}


    def parseFiles(self, trainFile, testFile):
        self.train = self.parseFile(trainFile)
        self.test = self.parseFile(testFile)


    def parseFile(self, fileName):
        lines = open(fileName, 'r').read().split('\n')

        data = []
        for line in lines:
            splitted = line.split(',')
            label = splitted[-1]
            strPoints = splitted[:-1]
            point = [int(num) for num in strPoints]
            point.append(splitted[-1])
            self.labels.add(label)
            data.append(point)
        return data


    def knn(self, k, d, unitw):
        for test in range(0, len(self.test)):
            distances = []
            for train in range(0, len(self.train)):
                curTest = self.test[test]
                curTrain = self.train[train]

                testCoordinate = curTest[:-1]
                trainCoordinate = curTrain[:-1]

                if d == 'e2':
                    dist = self.calculator.euclideanDistance(testCoordinate, trainCoordinate)
                    distances.append({dist:curTrain})
                elif d == 'manh':
                    dist = self.calculator.manhattanDistance(testCoordinate, trainCoordinate)
                    distances.append({dist:curTrain})

            # unit
            sortedDist = sorted(distances)
            neighbors = sortedDist[:k]
            newCluster = self.selectCluster(unitw, neighbors)
            print "want=" + self.test[test][-1] + " got=" + newCluster

            # Evaluation
            if newCluster in self.numGot:
                self.numGot[newCluster] += 1
            else:
                self.numGot[newCluster] = 1

            if self.test[test][-1] in self.numWant:
                self.numWant[self.test[test][-1]] += 1
            else:
                self.numWant[self.test[test][-1]] = 1

            if self.test[test][-1] == newCluster:
                if newCluster in self.numEquals:
                    self.numEquals[newCluster] += 1
                else:
                    self.numEquals[newCluster] = 1

        keys = list(self.labels)
        keys.sort()
        for key in keys:
            if key not in self.numWant:
                self.numWant[key] = 0
            if key not in self.numGot:
                self.numGot[key] = 0
            if key not in self.numEquals:
                self.numEquals[key] = 0

        for key in keys:
            print "Label=" + key + " Precision=" + str(self.numEquals[key]) + "/" + str(self.numGot[key]) + " Recall=" + str(self.numEquals[key]) + "/" + str(self.numWant[key])


    def selectCluster(self, unitw, neighbors):
        if unitw == 'unit':
            return self.selectClusterByUnit(neighbors)
        elif unitw == '1/d':
            return self.selectClusterByWeighted(neighbors)


    def selectClusterByUnit(self, neighbors):
        vote = {}
        for i in range(0, len(neighbors)):
            neighbor = neighbors[i].values()[0]
            if neighbor[-1] in vote:
                vote[neighbor[-1]] += 1
            else:
                vote[neighbor[-1]] = 1

        selected = max(vote, key=vote.get)

        #max_key = max(a_dictionary, key=a_dictionary.get)
        return selected


    def selectClusterByWeighted(self, neighbors):
        vote = {}
        for i in range(0, len(neighbors)):
            dist = neighbors[i].keys()[0]
            if dist == 0:
                dist = 1 / 0.0001
            else:
                dist = 1.0 / dist
            neighbor = neighbors[i].values()[0]
            if neighbor[-1] in vote:
                vote[neighbor[-1]] += dist
            else:
                vote[neighbor[-1]] = dist
        selected = max(vote, key=vote.get)
        return selected