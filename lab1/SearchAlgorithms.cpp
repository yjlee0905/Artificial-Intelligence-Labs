//
// Created by Yunjeon Lee on 2021/09/17.
//

#include <iostream>
#include <queue>
#include "SearchAlgorithms.h"

using namespace std;

void SearchAlgorithms::initVisited() {
    for (int i=0; i < MAX_VERTICES; i++) {
        visited[i] = false;
    }
}

void SearchAlgorithms::BFS(char start) {
    queue<char> q;

    initVisited();
    visited[convertToInt(start)] = true;
    cout << getVertex(convertToInt(start)) << " ";
    q.push(start);

    while (!q.empty()) {
        char vertex = q.front();
        q.pop();

        for (Node* n = getAdjListNode(convertToInt(vertex)); n != NULL; n = n->getLink()) {
            int adjNodeId = convertToInt(n->getName());
            if (!visited[adjNodeId]) {
                cout << getVertex(adjNodeId) << " ";
                visited[adjNodeId] = true;
                q.push(getVertex(adjNodeId));
            }
        }
    }
}
