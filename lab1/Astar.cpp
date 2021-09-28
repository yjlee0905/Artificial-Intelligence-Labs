//
// Created by Yunjeon Lee on 2021/09/28.
//

#include <iostream>
#include <cmath>
#include <float.h>
#include "Astar.h"

using namespace std;

bool Astar::isDestination(string cur, string goal) {
    if (cur.compare(goal) == 0) {
        return true;
    }
    return false;
}

double Astar::getEuclideanDistance(Node *start, Node *end) {
    return sqrt(pow(start->getXpos() - end->getXpos(), 2) + pow(start->getYpos() - end->getYpos(), 2));
}

bool Astar::isIncluded(string cur, vector<pair<string, double>> lst) {
    for (int i = 0; i < lst.size(); i++) {
        if (cur.compare(lst.at(i).first) == 0) {
            return true;
        }
    }
    return false;
}

int Astar::getIdxOfNodeWithLeastFvalue(vector<pair<string, double>> openLst) {
    double minVale = DBL_MAX;
    int idx;
    for (int i = 0; i < openLst.size(); ++i) {
        if (minVale > openLst.at(i).second) {
            minVale = openLst.at(i).second;
            idx = i;
        }
    }
    return idx;
}

void Astar::AstarAlgo(string start, string end) {
    vector<pair<string, double>> openList; // 생성되었으나 아직 검사하지 않은 노
    vector<pair<string, double>> closeList; // 검사할 노드를 포함

    // put startNode on the openList
//    vector<string> path;
//    path.push_back(start);

    pair<string, double> startPair;
    startPair.first = start;
    startPair.second = 0.0;

    openList.push_back(startPair);

    while (!openList.empty()) {
        // TODO open/close list에 넣을 때, 거리 계산할 것
        int idx = getIdxOfNodeWithLeastFvalue(openList);
        pair<string, double> curNode = openList.at(idx);
        openList.erase(openList.begin() + idx);

        closeList.push_back(curNode);

        if (isDestination(curNode.first, end)) {
            cout << "Reached the goal: " << curNode.first << endl;
        }

        vector<Node*> children = adjList.at(convertToOrder(curNode.first));
        for (int i = 0; i < children.size(); i++) {
            if (isIncluded(curNode.first, closeList)) {
                continue;
            }

            // TODO g
            float h = getEuclideanDistance(vertices[convertToOrder(curNode.first)], vertices[convertToOrder(end)]);
            // TODO f



        }
    }
}


