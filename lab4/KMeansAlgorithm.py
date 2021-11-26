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
        print newCentroids


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
            print('cluster: ', cluster)
            clusterDatas = decisions[cluster]

            if len(clusterDatas) == 0:
                centroids.append([0, 0])
                continue

            sumDatas = [0] * dimension
            newCentroid = []
            for data in clusterDatas:
                point = self.points[data]
                for i in range(0, len(point)):
                    sumDatas[i] += point[i]

            for j in range(0, len(sumDatas)):
                newCentroid.append(sumDatas[j] / len(decisions[cluster]))
            centroids.append(newCentroid)
        return centroids








        # centroids = []
        #
        # sumPoints = [0] * dimension
        # for cluster in decisions:
        #
        #     centroid = []
        #     for i in range(0, len(decisions[cluster])):
        #         for j in range(0, len(decisions[cluster])):
        #             point = decisions[cluster][j]
        #             for k in range(0, len(self.points[point])):
        #                 sumPoints[k] += self.points[point][k]
        #
        #             for k in range(0, len(sumPoints)):
        #                 centroid.append(sumPoints[i] / len(self.points))
        #     centroids.append(centroid)




    def euclideanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += pow(point1[i] - point2[i], 2)
        return dist