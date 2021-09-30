//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_BFS_H
#define AI_LABS_BFS_H

#include "Graph.h"

class BFS : public Graph {
private:
    vector<bool> visited;

    void initVisited();

public:
    vector<string> runAlgorithm(string start, string end, int startDepth);
};

#endif //AI_LABS_BFS_H