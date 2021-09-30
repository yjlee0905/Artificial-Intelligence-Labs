//
// Created by Yunjeon Lee on 2021/09/17.
//

#include <iostream>
#include <queue>
#include "BFS.h"

using namespace std;

void BFS::initVisited() {
    for (int i=0; i < getVerticesSize(); i++) {
        visited.push_back(false);
    }
}

vector<string> BFS::BFSalgo(string start, string end) {
    queue<string> q;
    vector<vector<string>> paths;

    initVisited();
    visited[convertToOrder(start)] = true;
    cout << "Expanding: " << getVertexName(convertToOrder(start)) << endl;
    vector<string> initialPath;
    initialPath.push_back(getVertexName(convertToOrder(start)));
    paths.push_back(initialPath);

    q.push(start);

    while (!q.empty()) {
        string vertex = q.front();
        q.pop();

        vector<string> toBeAdded;
        // vertex: parent, s: child
        for (int j = paths.size()-1; j >= 0; j--) {
            vector<string> path = paths.at(j);
            if (vertex.compare(path.at(path.size()-1)) == 0) {
                toBeAdded = path;
                break;
            }
        }

        // TODO start from 1?
        for (int i = 0; i < adjList.at(convertToOrder(vertex)).size(); i++) {
            string s = adjList.at(convertToOrder(vertex)).at(i)->getName();
            if (!visited[convertToOrder(s)]) {
                cout << "Expanding: " << getVertexName(convertToOrder(s)) << endl;
                vector<string> newPath = toBeAdded;
                newPath.push_back(s);
                paths.push_back(newPath);

                visited[convertToOrder(s)] = true;
                q.push(getVertexName(convertToOrder(s)));

                if (s.compare(end) == 0) {
                    return newPath;
                }
            }
        }
    }
}