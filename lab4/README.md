# Lab 4
The purpose this lab is to implement two algorithms
* KNN
* KMeans

## Dependencies
    Python3

## How to run

### KNN algorithm
#### Format
```
python knn.py -k {k value} -d {distance function} -unitw {voting weights} -train {train data file path} -test {test data file path}
```

#### Options
```
-k {k value}: k value, default = 3
-d {distance function}: distance function to use, values = [e2, manh]
-unitw {voting weights}: voting weights, values = [unit, 1/d]
-train {file path}: train data file path
-test {file path}: test data file path
```

#### Example
```
python knn.py -k 3 -d manh -uniw 1/d -train inputs/knn1.train.txt -test inputs/knn1.test.txt
```


### KMeans algorithm

#### Format
```
python kmeans.py -d {distance function} -data {file path} -c {centroids}
```

#### Options
```
-d {distance function}: distance function to use, values = [e2, manh]
-data {file path}: no default value and exit if file name is not specified
-c {centroids}: for the centroids, each coordinate should be separated by ',' and each point should be separated by empty space(' ')
```

#### Example
```
python kmeans.py -d e2 -data inputs/km2.txt -c "0,0,0 200,200,200 500,500,500"
```