//
// Created by Yunjeon Lee on 2021/10/15.
//

#ifndef ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H
#define ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H

#include <string>
#include <vector>
#include <set>

using namespace std;

class DPLLsolver {
private:
    vector<string> split(string target);

public:
    vector<vector<string>> parseSentences(vector<string> lines);
    vector<string> parseAtoms(vector<vector<string>> sentences);
};


#endif //ARTIFICIAL_INTELLIGENCE_LABS_DPLLSOLVER_H
