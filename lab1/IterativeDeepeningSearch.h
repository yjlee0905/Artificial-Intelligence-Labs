//
// Created by Yunjeon Lee on 2021/09/28.
//

#ifndef AI_LABS_ITERATIVEDEEPENINGSEARCH_H
#define AI_LABS_ITERATIVEDEEPENINGSEARCH_H

#include <stack>
#include "Graph.h"

class IterativeDeepeningSearch : public Graph {
private:
    vector<bool> visited; // for IDS

public:
    void initVisited();
    void clearVisited();
    void IDS(string start, string end, int startDepth);
    bool DFSrecursive(string start, string end, int curDepth, int depth, stack<string> path);





};

#endif //AI_LABS_ITERATIVEDEEPENINGSEARCH_H