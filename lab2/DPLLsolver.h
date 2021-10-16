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
    bool checkIsFailure(vector<vector<string>> parsed);
    map<string, int> findPureLiterals(vector<vector<string>> parsed, vector<string> atoms);
    void easyCaseSingle(map<string, string> result, vector<vector<string>> oneAtoms);
    vector<vector<string>> propagate(map<string, string> result, vector<vector<string>> parsed);



public:
    vector<vector<string>> parseSentences(vector<string> lines);
    vector<string> parseAtoms(vector<vector<string>> sentences);
    map<string, string> runDPLLalgorithm(vector<vector<string>> parsed, vector<string> atoms);

};


#endif //ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H
