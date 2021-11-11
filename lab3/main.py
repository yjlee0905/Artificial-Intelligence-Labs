from Parser import Parser

if __name__ == "__main__":
    print('start lab3')

    fileName = '/Users/yjeonlee/Desktop/[Fall2021]AI/AI-Python/lab3/inputs/maze.txt'

    parser = Parser()
    parser.parse(fileName)
    parser.parseAndValidateProbabilites()