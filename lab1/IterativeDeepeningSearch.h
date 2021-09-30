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
    void clearVisited();
    void DFS(string start, string end, int startDepth);
    bool DFSrecursive(string start, string end, int depth);


    // IDDFS
    bool DLS(string start, string end, int limit);
    bool IDDLS(string start, string end, int initialDepth, int maxDepth);

    // new way
    void iterativeDeepeningDFS(string start, string end);


};

#endif //AI_LABS_ITERATIVEDEEPENINGSEARCH_H