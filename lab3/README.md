# Lab 3
This lab is to implement
* Markov Process Solver

## Dependencies
    Python3

## How to run
### Format
```
python main.py -df {float} -min {True/False} -tol {tolerance} -iter {iteration} -file {file name}
```

### Options
```
-df {discount factor}: float, default=1.0
-min {min or max}: bool, default=False
-tol {tolerance}: float, default=0.01
-iter {iteration}: int, default=100
-file {file path}: string, no default value and exit if file name is not specified
```

### Examples
#### maze.txt
```
python main.py -tol 0.001 file inputs/maze.txt
```

#### restaurant.txt
```
python main.py -min True -tol 0.001 -file inputs/restaurant.txt
```

#### teach.txt
```
python main.py -df .9 -tol 0.001 -file inputs/teach.txt
```