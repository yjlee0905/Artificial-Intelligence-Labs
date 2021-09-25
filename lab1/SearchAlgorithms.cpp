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

void SearchAlgorithms::BFS(string start) {
    queue<string> q;

    initVisited();
    visited[convertToOrder(start)] = true;
    cout << getVertex(convertToOrder(start)) << " ";
    q.push(start);

    while (!q.empty()) {
        string vertex = q.front();
        q.pop();

        for (Node* n = getAdjListNode(convertToOrder(vertex)); n != NULL; n = n->getLink()) {
            int adjNodeId = convertToOrder(n->getName());
            if (!visited[adjNodeId]) {
                cout << getVertex(adjNodeId) << " ";
                visited[adjNodeId] = true;
                q.push(getVertex(adjNodeId));
            }
        }
    }
}
