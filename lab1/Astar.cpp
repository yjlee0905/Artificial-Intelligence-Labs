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

bool Astar::isIncluded(string cur, vector<pair<CalculationInfo, double>> lst) {
    for (int i = 0; i < lst.size(); i++) {
        if (cur.compare(lst.at(i).first.name) == 0) {
            return true;
        }
    }
    return false;
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

double Astar::calculateG(vector<string> path) {
    double distance = 0.0;
    for (int i = 0; i <= path.size()-2; i++) {
        distance += getEuclideanDistance(vertices[convertToOrder(path.at(i))], vertices[convertToOrder(path.at(i+1))]);
    }
    return distance;
}

vector<string> Astar::AstarAlgo(string start, string end) {
    vector<pair<vector<string>, double>> calculatedPaths; // 지금까지의 path, 거리

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
        if (curPath.first.at(curPath.first.size()-1).compare(end) == 0) {
            return curPath.first;
        }
        calculatedPaths.erase(calculatedPaths.begin() + idx);

        // expand curPath
        string lastNode = curPath.first.at(curPath.first.size()-1);
        vector<Node*> children = adjList.at(convertToOrder(lastNode));

        // curPath.first가 현재 list를 가지고 있음.
        for (int i = 1; i < children.size(); i++) {
            vector<string> tmpCurPath = curPath.first;
            tmpCurPath.push_back(children.at(i)->getName());

            double g = calculateG(tmpCurPath);
            double h = getEuclideanDistance(vertices[convertToOrder(children.at(i)->getName())], vertices[convertToOrder(end)]);
            double f = g + h;

            cout << lastNode << " -> " << children.at(i)->getName() << " ; g=" << g <<" h=" << h << " = " << f << endl;



            // calculate g
            // calculate h
            // push f value
            pair<vector<string>, double> newCaclulatedPath;
            newCaclulatedPath.first = tmpCurPath;
            newCaclulatedPath.second = f;
            calculatedPaths.push_back(newCaclulatedPath);
        }
    }


//    vector<pairstring, double>> openList; // 생성되었으나 아직 검사하지 않은 노
//    vector<pair<string, double>> closeList; // 검사할 노드를 포함
//
//    // put startNode on the openList
////    vector<string> path;
////    path.push_back(start);
//
//    pair<string, double> startPair;
//    startPair.first = start;
//    startPair.second = 0.0;
//
//    openList.push_back(startPair);
//
//    while (!openList.empty()) {
//        // TODO open/close list에 넣을 때, 거리 계산할 것
//        // open list에 있는 노드들 중 f의 값이 최소인 노드를 선
//        int idx = getIdxOfNodeWithLeastCost(openList);
//        pair<CalculationInfo, double> curNode = openList.at(idx);
//        openList.erase(openList.begin() + idx);
//
//        closeList.push_back(curNode);
//
//        if (isDestination(curNode.first.name, end)) {
//            cout << "Reached the goal: " << curNode.first.name << endl;
//        }
//
//        // g 값이 최소인 노드의 children을  expand
//        vector<Node*> children = adjList.at(convertToOrder(curNode.first.name));
////        vector<CalculationInfo> childrenInfos;
////        for (int i = 0; i < children.size(); i++) {
////            CalculationInfo info;
////            info.name = children.at(i)->getName();
////            info.xPos = children.at(i)->getXpos();
////            info.yPos = children.at(i)->getYpos();
////            info.path.push_back(curNode.first.name); // TODO check
////            info.g = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
////        }
//
//        for (int i = 0; i < children.size(); i++) {
//            if (isIncluded(curNode.first.name, closeList)) {
//                continue;
//            }
//
//            //double g = childrenInfos.at(i).g + getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
//            double g = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
//            double h = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(end)]);
//            double f = g + h;
//
//            if (isIncluded(children.at(i)->getName(), openList)) {
//                //if child.g is higher than the openList node's g
//                //continue to beginning of for loop
//            }
//            //openList.push_back();
//
//
//        }
//    }
}

//void AstarAlgo2(string start, string end) {
//    vector<pair<CalculationInfo, double>> openList; // 생성되었으나 아직 검사하지 않은 노드
//    vector<pair<CalculationInfo, double>> closeList; // 검사할 노드를 포함
//
//    // put startNode on the openList
////    vector<string> path;
////    path.push_back(start);
//
//    pair<CalculationInfo, double> startPair;
//    CalculationInfo startInfo;
//    startInfo.name = start;
//    startInfo.g = 0.0;
//    startPair.first = startInfo;
//    startPair.second = 0.0; // f
//
//    openList.push_back(startPair);
//
//    while (!openList.empty()) {
//        // TODO open/close list에 넣을 때, 거리 계산할 것
//        // open list에 있는 노드들 중 f의 값이 최소인 노드를 선
//        int idx = getIdxOfNodeWithLeastCost(openList);
//        pair<CalculationInfo, double> curNode = openList.at(idx);
//        openList.erase(openList.begin() + idx);
//
//        closeList.push_back(curNode);
//
//        if (isDestination(curNode.first.name, end)) {
//            cout << "Reached the goal: " << curNode.first.name << endl;
//        }
//
//        // g 값이 최소인 노드의 children을  expand
//        vector<Node*> children = adjList.at(convertToOrder(curNode.first.name));
////        vector<CalculationInfo> childrenInfos;
////        for (int i = 0; i < children.size(); i++) {
////            CalculationInfo info;
////            info.name = children.at(i)->getName();
////            info.xPos = children.at(i)->getXpos();
////            info.yPos = children.at(i)->getYpos();
////            info.path.push_back(curNode.first.name); // TODO check
////            info.g = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
////        }
//
//        for (int i = 0; i < children.size(); i++) {
//            if (isIncluded(curNode.first.name, closeList)) {
//                continue;
//            }
//
//            //double g = childrenInfos.at(i).g + getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
//            double g = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(children.at(i)->getName())]);
//            double h = getEuclideanDistance(vertices[convertToOrder(curNode.first.name)], vertices[convertToOrder(end)]);
//            double f = g + h;
//
//            if (isIncluded(children.at(i)->getName(), openList)) {
//                //if child.g is higher than the openList node's g
//                //continue to beginning of for loop
//            }
//            //openList.push_back();
//
//
//        }
//    }
//}



