from DistanceCalculator import DistanceCalculator

class KNNalgorithm:

    def __init__(self):
        self.train = []
        self.test = []
        self.calculator = DistanceCalculator()
        # {[p1, p2]: label}


    def parseFiles(self, trainFile, testFile):
        self.train = self.parseFile(trainFile)
        self.test = self.parseFile(testFile)


    def parseFile(self, fileName):
        lines = open(fileName, 'r').read().split('\n')

        data = []
        for line in lines:
            splitted = line.split(',')
            strPoints = splitted[:-1]
            point = [int(num) for num in strPoints]
            point.append(splitted[-1])
            data.append(point)
        return data


    def knn(self, k):
        for test in range(0, len(self.test)):
            distances = []
            for train in range(0, len(self.train)):
                curTest = self.test[test]
                curTrain = self.train[train]

                testCoordinate = curTest[:-1]
                trainCoordinate = curTrain[:-1]

                dist = self.calculator.manhattanDistance(testCoordinate, trainCoordinate)
                distances.append({dist:curTrain})

            # unit
            sortedDist = sorted(distances)
            neighbors = sortedDist[:k]
            newCluster = self.selectCluster(neighbors)
            print "want=" + self.test[test][-1] + " got=" + newCluster


    def selectCluster(self, neighbors):
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