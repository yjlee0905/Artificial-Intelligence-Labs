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
    bool isIncluded(string cur, vector<pair<string, double>> lst);

public:
    int getIdxOfNodeWithLeastFvalue(vector<pair<string, double>> openLst);
    void AstarAlgo(string start, string end);
};


#endif //AI_LABS_ASTAR_H
