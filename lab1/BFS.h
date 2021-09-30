//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_BFS_H
#define AI_LABS_BFS_H

#include "Graph.h"

class BFS : public Graph {
private:
    vector<bool> visited;

public:
    void initVisited();
    vector<string> BFSalgo(string start, string end);
};

#endif //AI_LABS_BFS_H