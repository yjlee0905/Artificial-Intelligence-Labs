
class KNNalgorithm:

    def __init__(self):
        self.points = []
        # {[p1, p2]: label}


    def parseFile(self, fileName):
        lines = open(fileName, 'r').read().split('\n')

        for line in lines:
            splitted = line.split(',')
            strPoints = splitted[:-1]
            point = [int(num) for num in strPoints]
            point.append(splitted[-1])
            self.points.append(point)
        print self.points


    def knn(self, k):
        for point in self.points:
            print("hello")


    def calculateCluster(self, k):

        shortestK = [0] * k

        for cur in range(0, len(self.points)):
            for comparision in range(0, len(self.points)):
                if cur == comparision:
                    continue


    def euclideanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += pow(point1[i] - point2[i], 2)
        return dist