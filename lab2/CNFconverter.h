//
// Created by Yunjeon Lee on 2021/10/14.
//

#ifndef ARTIFICIAL_INTELLIGENCE_LABS_CNFCONVERTER_H
#define ARTIFICIAL_INTELLIGENCE_LABS_CNFCONVERTER_H

#include <vector>
#include <regex>

using namespace std;

class CNFconverter {
private:
    vector<string> stack;

    // steps
    string decidePriorities(string sentence);

    pair<string, string> removeBrackets(string source, int id);


public:
    CNFconverter(string sentence);
    vector<string> doConvert(string);



};


#endif //ARTIFICIAL_INTELLIGENCE_LABS_CNFCONVERTER_H
