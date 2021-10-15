//
// Created by Yunjeon Lee on 2021/10/15.
//

#ifndef ARTIFICIAL_INTELLIGENCE_LABS_CONSTANTS_H
#define ARTIFICIAL_INTELLIGENCE_LABS_CONSTANTS_H

const string UNBOUNDED = "UNBOUNDED";

inline const set<string> getKeysFromMap (map<string, int> target) {
    set<string> keys;
    for (auto key : target) {
        keys.insert(key.first);
    }
    return keys;
}

#endif //ARTIFICIAL_INTELLIGENCE_LABS_CONSTANTS_H
