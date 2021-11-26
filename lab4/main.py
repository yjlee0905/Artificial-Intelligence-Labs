from KNNalgorithm import KNNalgorithm
from KMeansAlgorithm import KMeansAlgorithm

if __name__ == "__main__":
    print("Let's start lab4")

    #fileName = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/km2.txt"
    # kmeans = KMeansAlgorithm()
    # kmeans.parseFile(fileName)
    # kmeans.kmeans([[0,0,0], [200,200,200], [500,500,500]])

    fileName = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/knn1.train.txt"
    knn = KNNalgorithm()
    knn.parseFile(fileName)


