//
// Created by Yunjeon Lee on 2021/10/15.
//

#include "DPLLsolver.h"
#include "Constants.h"

using namespace std;

vector<vector<string>> DPLLsolver::parseSentences(vector<string> lines) {
    vector<vector<string>> parsedSentences;
    for (int i = 0; i < lines.size(); i++) {
        vector<string> parsed = split(lines.at(i));
        parsedSentences.push_back(parsed);
    }
    return parsedSentences;
}

vector<string> DPLLsolver::split(string target) {
    string delim = " ";
    vector<string> splited;
    int pos = 0;
    string token;
    while ((pos = target.find(delim)) != std::string::npos) {
        token = target.substr(0, pos);
        splited.push_back(token);
        target.erase(0, pos + delim.length());
    }

    // TODO eliminate whitespaces
    //const char whiteSpaces[] = " \t\r\n\v\g";
    //target.erase(remove(target.begin(), target.end(), whiteSpaces), target.end());
    if (target.length() > 0) {
        splited.push_back(target);
    }
    return splited;
}

vector<string> DPLLsolver::parseAtoms(vector<vector<string>> sentences) {
    set<string> atoms;

    for (int i = 0; i < sentences.size(); i++) {
        for (int j = 0; j < sentences.at(i).size(); j++) {
            string atom = sentences.at(i).at(j);
            if (atom.find('!') == 0) {
                atom = atom.substr(1, atom.size()-1);
            }
            atoms.insert(atom);
        }
    }

    vector<string> distinctAtoms{atoms.begin(), atoms.end()};
    return distinctAtoms;
}

bool DPLLsolver::runDPLLalgorithm(vector<vector<string>> parsed, vector<string> atoms) {
    // init atom states
    vector<pair<string, string>> atomStates;
    for (int i = 0; i < atoms.size(); i++) {
        pair<string, string> atomState;
        atomState.first = atoms.at(i);
        atomState.second = UNBOUNDED;
    }

    map<string, int> pure = findPureLiterals(parsed, atoms);
    // cout << pure.size() << endl;
}

map<string, int> DPLLsolver::findPureLiterals(vector<vector<string>> parsed, vector<string> atoms) {
    map<string, int> marks;
    for (int i = 0; i < atoms.size(); i++) {
        marks.insert({atoms.at(i), 0});
    }

    for (int i = 0; i < parsed.size(); i++) {
        for (int j = 0; j < parsed.at(i).size(); j++) {
            string atom = parsed.at(i).at(j);

            if (atom.find('!') == 0) {
                atom = atom.substr(1, atom.size()-1);
                set<string> keys = getKeysFromMap(marks);
                if (keys.find(atom) != keys.end()
                    && marks.find(atom)->second == 0) {
                    marks.at(atom) = -1;
                } else if ( keys.find(atom) != keys.end()
                        && marks.find(atom)->second == 1) {
                    marks.erase(atom);
                }
            } else {
                set<string> keys = getKeysFromMap(marks);
                if (keys.find(atom) != keys.end()
                    && marks.find(atom)->second == 0) {
                    marks.at(atom) = 1;
                } else if ( keys.find(atom) != keys.end()
                            && marks.find(atom)->second == -1) {
                    marks.erase(atom);
                }
            }
        }
    }
    // TODO check 0
    return marks;
}