//
// Created by Yunjeon Lee on 2021/10/14.
//
#include <iostream>
#include "CNFconverter.h"

using namespace std;

CNFconverter::CNFconverter(string sentence) {
    string final = sentence;
    while (1) {
        pair<string, string> removed = this->removeBrackets(sentence, this->stack.size());
        if (removed.first.empty()) break;
        final = sentence;
        this->stack.push_back(removed.second);
    }
    this->stack.push_back(final);
}

string CNFconverter::decidePriorities(string sentence) {
    bool flag = false;
    for (int i = 0; i < this->stack.size(); i++) {
        string newSrc = ""; // TODO add_brackets
        if (this->stack.at(i) != newSrc) {
            this->stack.at(i) = newSrc;
            flag = true;
        }
    }
    return "flag";
}

pair<string, string> CNFconverter::removeBrackets(string source, int id){
    regex re("\\(([^\\(]*?)\\)");
    smatch matched;
    if (regex_match(source, matched, re)) {
        for (int i = 0; i < matched.size(); i++) {
            cout << "Matched: " << matched[i].str() << endl;
        }
    }
}
