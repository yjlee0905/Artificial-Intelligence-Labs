//
// Created by Yunjeon Lee on 2021/10/14.
//

#include <iostream>
#include <fstream>
#include <vector>
#include "DPLLsolver.h"

using namespace std;

int main() {
    ifstream in;
    in.open("/Users/yjeonlee/Desktop/[Fall2021]AI/Artificial-Intelligence-Labs/lab2/inputs/dpexample3.txt");
    if (!in) {
        cerr << "Cannot open file!" << endl;
        exit(1);
    }

    vector<string> sentences;
    string line;
    while (getline(in, line)) {
        sentences.push_back(line);
    }

    DPLLsolver* solver = new DPLLsolver();
    vector<vector<string>> test1 = solver->parseSentences(sentences);
    vector<string> test2 = solver->parseAtoms(test1);

    cout << test1.size() << endl;
    cout << test2.size() << endl;

    in.close();
    return 0;
}

