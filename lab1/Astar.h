//
// Created by Yunjeon Lee on 2021/09/28.
//

#ifndef AI_LABS_ASTAR_H
#define AI_LABS_ASTAR_H

#include "Graph.h"

class Astar : public Graph {
private:
    bool isDestination(string cur, string goal);
    double getEuclideanDistance(Node* start, Node* end);
    double calculateG(vector<string> path);
    int getIdxOfNodeWithLeastCost(vector<pair<vector<string>, double>> calculated);
    void printCurPath(vector<string> path);

public:
    vector<string> runAlgorithm(string start, string end, int startDepth, bool isVerbose);
};

#endif //AI_LABS_ASTAR_H