
class DistanceCalculator:

    def euclideanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += pow(point1[i] - point2[i], 2)
        return dist


    def manhattanDistance(self, point1, point2):
        dist = 0
        for i in range(0, len(point1)):
            dist += abs(point1[i] - point2[i])
        return dist