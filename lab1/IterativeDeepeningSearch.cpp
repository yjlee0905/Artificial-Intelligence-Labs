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

void IterativeDeepeningSearch::clearVisited() {
    for (int i = 0; i < getVerticesSize(); i++) {
        visited.at(i) = false;
    }
}


void IterativeDeepeningSearch::DFS(string start, string end, int startDepth) {
    initVisited();
//    for (int limit = startDepth; limit <=4 ; limit++) {
//        DFSrecursive(start, end, limit);
//    }
    //DFSrecursive(start, end, startDepth);
    //DFSrecursive(start, end, startDepth+1);

    while (true) {
        clearVisited();
        if (DFSrecursive(start, end, startDepth, startDepth++)) {
            return;
        }
    }
}

bool IterativeDeepeningSearch::DFSrecursive(string start, string end, int curDepth, int depth) {
    visited[convertToOrder(start)] = true; // 현재 vertex 방문 처리

    if (start.compare(end) == 0) {
        return true;
    }

    if (curDepth <= 0) {
        cout << "hit depth=" << depth << ": " << start << endl;
        return false;
    }

    cout << "Expand: " << start << endl;

    vector<Node*> adjInfo = adjList.at(convertToOrder(start));
    for (int i = 1; i < adjInfo.size(); i++) {
        if (visited[convertToOrder(adjInfo.at(i)->getName())] == false) {
            if (DFSrecursive(adjInfo.at(i)->getName(), end, curDepth-1, depth) == true) {
                return true;
            }
        }
    }
    return false;
}

bool IterativeDeepeningSearch::DLS(string start, string end, int limit) {
    if (start.compare(end) == 0) {
        return true;
    }

    if (limit <= 0) {
        return false;
    }

    vector<Node*> lst = adjList.at(convertToOrder(start));
    for (int i = 0; i < lst.size(); i++) {
        if (DLS(lst.at(i)->getName(), end, limit)) {
            return true;
        }
    }
    return false;
}

bool IterativeDeepeningSearch::IDDLS(string start, string end, int initialDepth, int maxDepth) {
    for (int depth = initialDepth; depth <= maxDepth; depth++) {
        if (DLS(start, end, depth) == true) {
            return true;
        }
    }
    return false;
}