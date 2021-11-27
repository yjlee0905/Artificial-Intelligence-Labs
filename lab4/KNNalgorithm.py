
class KNNalgorithm:

    def __init__(self):
        self.train = []
        self.test = []
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

                dist = self.euclideanDistance(testCoordinate, trainCoordinate)
                distances.append({dist:curTrain})

            # unit
            sortedDist = sorted(distances)
            neighbors = sortedDist[:k]
            newCluster = self.selectCluster(neighbors)
            print "want=" + self.test[test][-1] + " got=" + newCluster



    def decideCluster(self, k):
        distances = [] # {distance : point}
        for cur in range(0, len(self.train)):
            for comparision in range(0, len(self.train)):
                if cur == comparision:
                    continue
                curPoint = self.train[cur]
                comparisionPoint = self.train[comparision]
                curCoordinate = curPoint[:-1]
                compCoordinate = comparisionPoint[:-1]
                dist = self.euclideanDistance(curCoordinate, compCoordinate)
                distances.append({dist:comparisionPoint})

            sortedDist = sorted(distances)
            neighbors = sortedDist[:k]
            newCluster = self.selectCluster(neighbors)

            print newCluster


    def euclideanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += pow(point1[i] - point2[i], 2)
        return dist


    def selectCluster(self, neighbors):
        vote = {}
        for i in range(0, len(neighbors)):
            neighbor = neighbors[i].values()[0]
            if neighbor[-1] in vote:
                vote[neighbor[-1]] += 1
            else:
                vote[neighbor[-1]] = 1

        selected = max(vote)
        return selected