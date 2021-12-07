import sys
from DistanceCalculator import DistanceCalculator

class KMeansAlgorithm:

    def __init__(self):
        self.points = {}
        self.calculator = DistanceCalculator()

    def parseFile(self, fileName):
        # TODO check file format, not csv
        lines = open(fileName, 'r').read().split('\n')

        for line in lines:
            splitted = line.split(',')
            # TODO check, A1, A2 always distinct?
            strPoints = splitted[:-1]
            # TODO check points are always int
            numPoints = [int(num) for num in strPoints]
            self.points[splitted[-1]] = numPoints


    def kmeans(self, d, initialCentroids):
        prevDecisions = None
        curDecisions = self.decideCluster(d, initialCentroids)
        prevCentroids = initialCentroids
        while prevDecisions != curDecisions:
            # TODO check
            newCentroids = self.updateCentroids(curDecisions, len(initialCentroids[0]), prevCentroids)
            prevDecisions = curDecisions
            curDecisions = self.decideCluster(d, newCentroids)
            prevCentroids = newCentroids

        # print result
        for curDecision in curDecisions:
            curDecisions[curDecision].sort()
            print curDecisions[curDecision]

        for centroid in newCentroids:
            print centroid


    def decideCluster(self, d, centroids):
        decisions = {}
        for i in range(0, len(centroids)):
            decisions[i] = []

        for point in self.points:
            cluster = -1
            minVal = sys.maxint
            for i in range(0, len(centroids)):
                curDist = self.calculator.manhattanDistance(centroids[i], self.points[point]) if d == 'manh' else self.calculator.euclideanDistance(centroids[i], self.points[point])
                if minVal > curDist:
                    minVal = curDist
                    cluster = i
            decisions[cluster].append(point)

        return decisions


    def updateCentroids(self, decisions, dimension, prevCentroids):

        centroids = []
        for cluster in decisions:
            clusterDatas = decisions[cluster]

            if len(clusterDatas) == 0:
                centroids.append(prevCentroids[cluster])
                #centroids.append([0] * dimension) # TODO check
                continue

            sumDatas = [0] * dimension
            newCentroid = []
            for data in clusterDatas:
                point = self.points[data]
                for i in range(0, len(point)):
                    sumDatas[i] += point[i]

            for j in range(0, len(sumDatas)):
                newCentroid.append(float(sumDatas[j]) / len(decisions[cluster]))
            centroids.append(newCentroid)
        return centroids