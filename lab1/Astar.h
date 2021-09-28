//
// Created by Yunjeon Lee on 2021/09/28.
//

#ifndef AI_LABS_ASTAR_H
#define AI_LABS_ASTAR_H

#include "Graph.h"

struct CalculationInfo{
    string name;
    int xPos;
    int yPos;
    double g;
    vector<string> path;
};


class Astar : public Graph {
private:
    bool isDestination(string cur, string goal);
    double getEuclideanDistance(Node* start, Node* end);
    bool isIncluded(string cur, vector<pair<CalculationInfo, double>> lst);
    double calculateG(vector<string> path);

public:
    int getIdxOfNodeWithLeastCost(vector<pair<vector<string>, double>> calculated);
    vector<string> AstarAlgo(string start, string end);
};


#endif //AI_LABS_ASTAR_H
