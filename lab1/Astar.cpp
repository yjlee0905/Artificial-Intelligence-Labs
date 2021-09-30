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

double Astar::calculateG(vector<string> path) {
    double distance = 0.0;
    for (int i = 0; i <= path.size()-2; i++) {
        distance += getEuclideanDistance(vertices[convertToOrder(path.at(i))], vertices[convertToOrder(path.at(i+1))]);
    }
    return distance;
}

int Astar::getIdxOfNodeWithLeastCost(vector<pair<vector<string>, double>> calculated) {
    double minVale = DBL_MAX;
    int idx;
    for (int i = 0; i < calculated.size(); i++) {
        if (minVale > calculated.at(i).second) {
            minVale = calculated.at(i).second;
            idx = i;
        }
    }
    return idx;
}

void Astar::printCurPath(vector<string> path) {
    cout << "adding ";
    for (int i = 0; i < path.size(); i++) {
        if (i == path.size()-1) {
            cout << path.at(i);
        } else {
            cout << path.at(i) << " -> ";
        }
    }
    cout << endl;
}

vector<string> Astar::AstarAlgo(string start, string end) {
    vector<pair<vector<string>, double>> calculatedPaths;

    // set start node
    vector<string> startNode;
    startNode.push_back(start);
    pair<vector<string>, double> startPath;
    startPath.first = startNode;
    startPath.second = 0.0;
    calculatedPaths.push_back(startPath);

    while (true) {
        int idx = getIdxOfNodeWithLeastCost(calculatedPaths);
        pair<vector<string>, double> curPath = calculatedPaths.at(idx);
        if (isDestination(curPath.first.at(curPath.first.size()-1), end)) {
            return curPath.first;
        }
        calculatedPaths.erase(calculatedPaths.begin() + idx);

        printCurPath(curPath.first);

        // expand curPath
        string lastNode = curPath.first.at(curPath.first.size()-1);
        vector<Node*> children = adjList.at(convertToOrder(lastNode));

        // curPath.first contains path
        for (int i = 1; i < children.size(); i++) {
            vector<string> tmpCurPath = curPath.first;
            tmpCurPath.push_back(children.at(i)->getName());

            double g = calculateG(tmpCurPath);
            double h = getEuclideanDistance(vertices[convertToOrder(children.at(i)->getName())], vertices[convertToOrder(end)]);
            double f = g + h;

            printf("%s -> %s ; g=%.2lf h=%.2lf = %.2lf\n",
                   lastNode.c_str(), children.at(i)->getName().c_str(), g, h, f);
            //cout << lastNode << " -> " << children.at(i)->getName() << " ; g=" << g <<" h=" << h << " = " << f << endl;

            pair<vector<string>, double> newCaclulatedPath;
            newCaclulatedPath.first = tmpCurPath;
            newCaclulatedPath.second = f;
            calculatedPaths.push_back(newCaclulatedPath);
        }
    }
}