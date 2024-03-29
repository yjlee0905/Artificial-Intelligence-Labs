//
// Created by Yunjeon Lee on 2021/09/17.
//

#include <iostream>
#include "Graph.h"

using namespace std;

Node::Node(string name, int xPos, int yPos) {
    this->name = name;
    this->xPos = xPos;
    this->yPos = yPos;
}

string Node::getName() {
    return name;
}

int Node::getXpos() {
    return xPos;
}

int Node::getYpos() {
    return yPos;
}

Graph::Graph() {
    this->size = 0;
    // initialize parsedVertices
    for (int i = 0; i < vertices.size(); i++) {
        vertices.at(i) = nullptr; // TODO check later
    }
}

int Graph::getVerticesSize() {
    return size;
}

int Graph::convertToOrder(string name) {
    for (int i = 0; i < vertices.size(); i++) {
        if (vertices[i]->getName().compare(name) == 0) {
            return i;
        }
    }
    return -1;
}

void Graph::insertVertex(string name, int xPos, int yPos) {
    int targetIdx = -1;
    for (int i = 0;  i < vertices.size(); i++) {
        if (name.compare(vertices.at(i)->getName()) < 0) {
            targetIdx = i;
            break;
        }
    }
    Node* newNode = new Node(name, xPos, yPos);
    if (targetIdx != -1) {
        vertices.insert(vertices.begin() + targetIdx, newNode);
    } else {
        vertices.push_back(newNode);
    }

    size++;
}

string Graph::getVertexName(int idx) {
    return vertices.at(idx)->getName();
}

void Graph::insertEdge(string start, string end) {
    int startOrder = convertToOrder(start);
    int endOrder = convertToOrder(end);

    if (startOrder == -1 || endOrder == -1) {
        cout << "Edge referencing a vertex not in the file" << endl;
        exit(1);
    }

    // insert to start adjList
    int targetIdx = -1;
    for (int i=1; i<adjList[startOrder].size(); i++) {
        if (end.compare(adjList[startOrder].at(i)->getName()) < 0) {
            targetIdx = i;
            break;
        }
    }

    // insert x, y position only in vertices, because the order of input file varies.
    if (targetIdx != -1) {
        adjList[startOrder].insert(adjList[startOrder].begin() + targetIdx, new Node(end, 0, 0));
    } else {
        adjList[startOrder].push_back(new Node(end, 0, 0));
    }

    // insert to end adjList
    targetIdx = -1;
    for (int i=1; i<adjList[endOrder].size(); i++) {
        if (start.compare(adjList[endOrder].at(i)->getName()) < 0) {
            targetIdx = i;
            break;
        }
    }

    if (targetIdx != -1) {
        adjList[endOrder].insert(adjList[endOrder].begin() + targetIdx, new Node(start, 0, 0));
    } else {
        adjList[endOrder].push_back(new Node(start, 0, 0));
    }
}

void Graph::createAdjList(vector<Node*> parsed) {
    for (int i=0; i<vertices.size(); i++) {
        int x, y;
        for (int j = 0; j < parsed.size(); ++j) {
            if (vertices.at(i)->getName().compare(parsed.at(j)->getName()) == 0) {
                x = parsed.at(j)->getXpos();
                y = parsed.at(j)->getYpos();
                break;
            }
        }

        vector<Node*> nodeList;
        Node* startNode = new Node(vertices.at(i)->getName(), x, y);
        nodeList.push_back(startNode);
        adjList.push_back(nodeList);
    }
}

void Graph::display() {
    for (int i = 0; i < adjList.size(); i++) {
        for (int j = 0; j < adjList.at(i).size(); j++) {
            if (j == 0) {
                cout << adjList.at(i).at(j)->getName() << ": ";
            } else {
                cout << adjList.at(i).at(j)->getName() <<  " ";
            }
        }
        cout << endl;
    }
}

vector<string> Graph::runAlgorithm(string start, string end, int startDepth, bool isVerbose) {}