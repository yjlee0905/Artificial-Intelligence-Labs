//
// Created by Yunjeon Lee on 2021/10/15.
//

#ifndef ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H
#define ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

class DPLLsolver {
private:
    vector<string> split(string target);
    map<string, int> findPureLiterals(vector<vector<string>> parsed, vector<string> atoms);


public:
    vector<vector<string>> parseSentences(vector<string> lines);
    vector<string> parseAtoms(vector<vector<string>> sentences);
    bool runDPLLalgorithm(vector<vector<string>> parsed, vector<string> atoms);

};


#endif //ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H
