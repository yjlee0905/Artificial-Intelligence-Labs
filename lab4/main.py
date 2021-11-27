from KNNalgorithm import KNNalgorithm
from KMeansAlgorithm import KMeansAlgorithm

if __name__ == "__main__":

    # fileName = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/km1.txt"
    # kmeans = KMeansAlgorithm()
    # kmeans.parseFile(fileName)
    # kmeans.kmeans([[0,0], [200,200], [500,500]])

    train = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/knn3.train.txt"
    test = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/knn3.test.txt"
    knn = KNNalgorithm()
    knn.parseFiles(train, test)
    knn.knn(3)


