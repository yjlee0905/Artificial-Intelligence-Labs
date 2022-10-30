# Lab 2
This lab has three modes as below:
* BNF to CNF converter
* Generic DPLL solver
* take BNF as an input and solve it by running above two modes

## Dependencies
    Python3

## How to run
### Format
```
python main.py -mode {mode} -file {file name} [-v]
```

### Options
```
-mode {mode name}: name of the mode  values: [cnf, dpll, solver]
-file {file path}: name of the input file
-v {True/False} : verbose mode  values: [True, False]
```

### Examples
#### BNF to CNF converter
```
python main.py -mode cnf -file inputs/example1.txt
```

#### Generic DPLL solver
```
python main.py -mode dpll -file inputs/dpexample3.txt
```

#### take BNF as an input and solve it by running above two modes
```
python main.py -mode solver -file inputs/example1.txt
```


        