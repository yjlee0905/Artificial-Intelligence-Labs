//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_SEARCHALGORITHMS_H
#define AI_LABS_SEARCHALGORITHMS_H

#include "Graph.h"

class SearchAlgorithms : public Graph {
private:
    vector<bool> visited;

public:
    void initVisited();
    void BFS(string start, string end);
};

#endif //AI_LABS_SEARCHALGORITHMS_H
