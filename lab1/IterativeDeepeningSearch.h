//
// Created by Yunjeon Lee on 2021/09/28.
//

#ifndef AI_LABS_ITERATIVEDEEPENINGSEARCH_H
#define AI_LABS_ITERATIVEDEEPENINGSEARCH_H

#include "Graph.h"

class IterativeDeepeningSearch : public Graph {
private:
    vector<bool> visited; // for DFS

public:
    void initVisited();
    void DFS(string start);
    void DFSrecursive(string start);
};

#endif //AI_LABS_ITERATIVEDEEPENINGSEARCH_H