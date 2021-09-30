//
// Created by Yunjeon Lee on 2021/09/28.
//

#include <iostream>
#include <stack>
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

vector<string> IterativeDeepeningSearch::runAlgorithm(string start, string end, int startDepth) {
    stack<string> resPath;
    vector<string> empty;

    initVisited();

    while (true) {
        clearVisited();
        if (DFSrecursive(start, end, startDepth, startDepth++, resPath)) {
            return empty;
        }
    }
}

bool IterativeDeepeningSearch::DFSrecursive(string start, string end, int curDepth, int depth, stack<string> path) {
    visited[convertToOrder(start)] = true;
    path.push(start);

    if (start.compare(end) == 0) {

        stack<string> reverseOrder;
        while (!path.empty()) {
            reverseOrder.push(path.top());
            path.pop();
        }

        cout << "Solution: ";
        while (!reverseOrder.empty()) {
            if (reverseOrder.size() == 1) {
                cout << reverseOrder.top();
            } else {
                cout << reverseOrder.top() << " -> ";
            }
            reverseOrder.pop();
        }
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
            if (DFSrecursive(adjInfo.at(i)->getName(), end, curDepth-1, depth, path) == true) {
                return true;
            }
        }
    }
    path.pop();
    return false;
}