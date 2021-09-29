//
// Created by Yunjeon Lee on 2021/09/28.
//

#include <iostream>
#include "IterativeDeepeningSearch.h"

using namespace std;

void IterativeDeepeningSearch::initVisited() {
    for (int i = 0; i < getVerticesSize(); i++) {
        visited.push_back(false);
    }
}

void IterativeDeepeningSearch::DFS(string start) {
    initVisited();
    DFSrecursive(start);
}

void IterativeDeepeningSearch::DFSrecursive(string start) {
    visited[convertToOrder(start)] = true; // 현재 vertex 방문 처리
    cout << start <<  " ";

    vector<Node*> adjInfo = adjList.at(convertToOrder(start));
    for (int i = 1; i < adjInfo.size(); i++) {
        if (visited[convertToOrder(adjInfo.at(i)->getName())] == false) {
            DFSrecursive(adjInfo.at(i)->getName());
        }
    }
}
