import sys

class KMeansAlgorithm:

    def __init__(self):
        self.points = {}

    def parseFile(self, fileName):
        # TODO check file format
        lines = open(fileName, 'r').read().split('\n')

        for line in lines:
            splitted = line.split(',')
            # TODO check, A1, A2 always distinct?
            strPoints = splitted[:-1]
            # TODO check points are always int
            numPoints = [int(num) for num in strPoints]
            self.points[splitted[-1]] = numPoints

        print len(self.points)

    def kmeans(self, initialPoints):
        prevDecisions = None
        curDecisions = self.decideCluster(initialPoints)
        while prevDecisions != curDecisions:
            newCentroids = self.updateCentroids(curDecisions, len(initialPoints[0]))
            prevDecisions = curDecisions
            curDecisions = self.decideCluster(newCentroids)
        print curDecisions


    def decideCluster(self, centroids):
        decisions = {}
        for i in range(0, len(centroids)):
            decisions[i] = []

        for point in self.points:
            cluster = -1
            minVal = sys.maxint
            for i in range(0, len(centroids)):
                curDist = self.euclideanDistance(centroids[i], self.points[point])
                if minVal > curDist:
                    minVal = curDist
                    cluster = i
            # if len(decisions[cluster]) == 0:
            #     decisions[cluster] = set(point)
            # else:
            decisions[cluster].append(point)

        return decisions

    def updateCentroids(self, decisions, dimension):
        centroids = []

        for cluster in decisions:
            sumPoints = [0] * dimension
            centroid = []
            for i in range(0, len(decisions[cluster])):
                for j in range(0, len(decisions[cluster])):
                    point = decisions[cluster][j]
                    for k in range(0, len(self.points[point])):
                        sumPoints[k] += self.points[point][k]

                    for k in range(0, len(sumPoints)):
                        centroid.append(sumPoints[i] / len(self.points))
            centroids.append(centroid)

        return centroids


    def euclideanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += pow(point1[i] - point2[i], 2)
        return dist