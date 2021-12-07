import argparse
from KMeansAlgorithm import KMeansAlgorithm

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str)
    parser.add_argument('-data', type=str)
    parser.add_argument('-c', type=str)

    args = parser.parse_args()
    d = args.d
    dataFile = args.data
    c = args.c

    centroids = []
    points = c.split(' ')
    for point in points:
        centroid = point.split(',')
        centroids.append(centroid)

    #fileName = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/km1.txt"

    kmeans = KMeansAlgorithm()
    kmeans.parseFile(dataFile)
    kmeans.kmeans(centroids)




