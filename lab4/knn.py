import argparse
from KNNalgorithm import KNNalgorithm

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-k', type=int, default=3)
    parser.add_argument('-d', type=str)
    parser.add_argument('-unitw', type=str)
    parser.add_argument('-train', type=str)
    parser.add_argument('-test', type=str)

    args = parser.parse_args()
    k = args.k
    d = args.d
    unitw = args.unitw
    trainFile = args.train
    testFile = args.test

    knn = KNNalgorithm()
    knn.parseFiles(trainFile, testFile)
    knn.knn(k, d, unitw)

    # train = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/knn3.train.txt"
    # test = "/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab4/inputs/knn3.test.txt"
    # knn = KNNalgorithm()
    # knn.parseFiles(train, test)
    # knn.knn(7)