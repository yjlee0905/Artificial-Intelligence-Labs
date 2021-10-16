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

map<string, string> DPLLsolver::runDPLLalgorithm(vector<vector<string>> parsed, vector<string> atoms) {
    map<string, string> result;
    // init atom states
    vector<pair<string, string>> atomStates; // oAssign
    for (int i = 0; i < atoms.size(); i++) {
        pair<string, string> atomState;
        atomState.first = atoms.at(i);
        atomState.second = UNBOUNDED;
    }

    map<string, int> pure = findPureLiterals(parsed, atoms);
    // cout << pure.size() << endl;

    // solve 1 atom
    vector<vector<string>> oneAtomSentence;
    for (int i = 0; i < parsed.size(); i++) {
        if (parsed.at(i).size() == 1) {
            oneAtomSentence.push_back(parsed.at(i));
        }
    }

    bool isOneAtomSentence = !oneAtomSentence.empty();
    bool isSuccess = parsed.empty();
    bool isFailure = checkIsFailure(parsed);

    while (isOneAtomSentence || isSuccess || isFailure || !pure.empty()) {
        if (isSuccess) {
            for (int i = 0; i < atoms.size(); i++) {
                if (result.find(atoms.at(i))->second.compare(UNBOUNDED) == 0) {
                    result.at(atoms.at(i)) = FALSE;
                }
            }
            result.insert({RESULT, SUCCESS});
            return result;
        } else if (isFailure) {
            result.insert({RESULT, FAILURE});
            return result;
        } else {
            if (isOneAtomSentence) {
                easyCaseSingle(result, oneAtomSentence);
                // vector<vector<string>> copied = parsed;
                parsed = propagate(result, parsed);
            } else if (!pure.empty()) {

            }

        }
    }




}

bool DPLLsolver::checkIsFailure(vector<vector<string>> parsed) {
    for (int i = 0; i < parsed.size(); i++) {
        if (parsed.at(i).size() != 0) {
            return true;
        }
    }
    return false;
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
                if (keys.find(atom) != keys.end() && marks.find(atom)->second == 0) {
                    marks.at(atom) = -1;
                } else if ( keys.find(atom) != keys.end() && marks.find(atom)->second == 1) {
                    marks.erase(atom);
                }
            } else {
                set<string> keys = getKeysFromMap(marks);
                if (keys.find(atom) != keys.end() && marks.find(atom)->second == 0) {
                    marks.at(atom) = 1;
                } else if ( keys.find(atom) != keys.end() && marks.find(atom)->second == -1) {
                    marks.erase(atom);
                }
            }
        }
    }
    // TODO check 0
    return marks;
}

void DPLLsolver::easyCaseSingle(map<string, string> result, vector<vector<string>> oneAtoms) {
    for (int i = 0; i < oneAtoms.size(); i++) {
        string atom = oneAtoms.at(i).at(0);
        if (atom.find('!') == 0) {
            if (result.at(atom.substr(1, atom.size()-1)).compare(UNBOUNDED) == 0) {
                result.at(atom.substr(1, atom.size()-1)) = FALSE;
            }
        } else {
            if (result.at(atom).compare(UNBOUNDED) == 0) {
                result.at(atom) = TRUE;
            }
        }
    }
}

vector<vector<string>> DPLLsolver::propagate(map<string, string> result, vector<vector<string>> parsed) {

    int i = 0;
    while (!parsed.empty() && i < parsed.size()) {
        vector<string> sentence = parsed.at(i);
        bool isIincrement = true;

        int j = 0;
        while (!parsed.at(i).empty() && j < parsed.at(i).size()) {
            bool isJincrement = true;
            string each = sentence.at(j);

            if (each.find('!') == 0) {
                each = each.substr(1, each.size()-1);
                if (result.at(each).compare(FALSE) == 0) {
                    parsed.erase(parsed.begin() + i); // TODO check
                    isIincrement = false;
                    break;
                } else if (result.at(each).compare(TRUE) == 0) {
                    parsed.at(i).erase(parsed.at(i).begin() + j);
                    isJincrement = false;
                }
            } else {
                if (result.at(each).compare(TRUE) == 0) {
                    parsed.erase(parsed.begin() + i);
                    isIincrement = false;
                    break;
                } else if (result.at(each).compare(FALSE) == 0) {
                    parsed.at(i).erase(parsed.at(i).begin() + j);
                    isJincrement = false;
                }

            }

            if (isJincrement) j++;
        }
        if (isIincrement) i++;
    }
    return parsed;
}