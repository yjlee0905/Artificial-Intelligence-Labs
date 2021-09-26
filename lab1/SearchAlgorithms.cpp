//
// Created by Yunjeon Lee on 2021/09/17.
//

#include <iostream>
#include <queue>
#include "SearchAlgorithms.h"

using namespace std;

void SearchAlgorithms::initVisited() {
    for (int i=0; i < getVerticesSize(); i++) {
        visited.push_back(false);
    }
}

void SearchAlgorithms::BFS(string start, string end) {
    queue<string> q;

    initVisited();
    visited[convertToOrder(start)] = true;
    cout << "Expanding: " << getVertex(convertToOrder(start)) << endl;
    q.push(start);

    while (!q.empty()) {
        string vertex = q.front();
        q.pop();

        for (int i = 0; i < adjList.at(convertToOrder(vertex)).size(); i++) {
            string s = adjList.at(convertToOrder(vertex)).at(i)->getName();
            if (!visited[convertToOrder(s)]) {
                cout << "Expanding: " << getVertex(convertToOrder(s)) << endl;
                visited[convertToOrder(s)] = true;
                q.push(getVertex(convertToOrder(s)));
            }
        }

//        for (Node* n = getAdjListNode(convertToOrder(vertex)); n != NULL; n = n->getLink()) {
//            int adjNodeId = convertToOrder(n->getName());
//            if (!visited[adjNodeId]) {
//                cout << getVertex(adjNodeId) << " ";
//                visited[adjNodeId] = true;
//                q.push(getVertex(adjNodeId));
//            }
//        }
    }
}
