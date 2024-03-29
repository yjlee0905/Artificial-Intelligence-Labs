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

vector<string> IterativeDeepeningSearch::runAlgorithm(string start, string end, int startDepth, bool isVerbose) {
    stack<string> resPath;
    vector<string> empty;

    if (convertToOrder(start) == -1) {
        cout << "-s referencing a vertex not in the graph file" << endl;
        exit(1);
    }

    if (convertToOrder(end) == -1) {
        cout << "-e referencing a vertex not in the graph file" << endl;
        exit(1);
    }

    if (startDepth == -1) {
        cout << "-d[initial depth] is omitted for the option. Just start with depth=1" << endl;
        startDepth = 1;
    }

    initVisited();

    startDepth = startDepth - 1;

    while (true) {
        clearVisited();
        if (DFSrecursive(start, end, startDepth, ++startDepth, resPath, isVerbose)) {
            return empty;
        }
    }
}

bool IterativeDeepeningSearch::DFSrecursive(string start, string end, int curDepth, int depth, stack<string> path, bool isVerbose) {
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
        cout << endl;
        return true;
    }

    if (curDepth <= 0) {
        if (isVerbose) {
            cout << "hit depth=" << depth << ": " << start << endl;
        }
        return false;
    }

    if (isVerbose) {
        cout << "Expand: " << start << endl;
    }

    vector<Node*> adjInfo = adjList.at(convertToOrder(start));
    for (int i = 1; i < adjInfo.size(); i++) {
        if (visited[convertToOrder(adjInfo.at(i)->getName())] == false) {
            if (DFSrecursive(adjInfo.at(i)->getName(), end, curDepth-1, depth, path, isVerbose) == true) {
                return true;
            }
        }
    }
    path.pop();
    return false;
}