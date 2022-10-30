# Lab 1
The purpose of this lab is to implement three search algorithms
    - Breadth First Search
    - Iterative Deepening Search
    - A* Search

## Dependencies
    - C++11

## How to run code
### Format
```
make lab1
./lab1 [-v] -a{algorithm} -s{start node} -e{goal node} [-d{depth}] graph-file
```

### Options
```
-v : verbose
-s{start node}: set start node
-e{end node}: set goal node
-a{algorithm}:
    B: Breadth First Search
    I: Iterative Deepening Search
    A: A* Search
-d[depth]: set initial depth for Iterative Deepening Search (default=1)
```

### Examples
#### Breadth First Search
```
./lab1 -aB -sS -eG inputs/ex1.txt
```

#### Iterative Deepening Search
```
./lab1 -aI -sS -eG -d2 inputs/ex1.txt
```

#### A* Search
```
./lab1 -aA -sS -eG inputs/ex1.txt
```

