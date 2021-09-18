//
// Created by Yunjeon Lee on 2021/09/17.
//

#include <iostream>
#include "Graph.h"

using namespace std;

//Node::Node(char name, int xPos, int yPos, Node *link) {
//    this->name = name;
//    this->xPos = xPos;
//    this->yPos = yPos;
//    this->link = link;
//}

Node::Node(char name, Node *link) {
    this->name = name;
    this->link = link;
}

void Node::setLink(Node *link) {
    this->link = link;
}

Node* Node::getLink() {
    return link;
}

char Node::getName() {
    return name;
}

Graph::Graph() {
    this->size = 0;
    // initialize vertices
    for (int i = 0; i < MAX_VERTICES; ++i) {
        vertices[i] = -1;
    }
}

int Graph::convertToInt(char name) {
    return name - 'A';
}

char Graph::convertToChar(int idx) {
    return idx + 'A';
}

void Graph::insertVertex(char name) {
    // TODO Graph validation check : graph full?
    vertices[convertToInt(name)] = name;
    adjList[convertToInt(name)] = nullptr;
    size++;
}

void Graph::insertEdge(char u, char v) {
    int uNum = convertToInt(u);
    int vNum = convertToInt(v);

    adjList[uNum] = new Node(v, adjList[uNum]);
    adjList[vNum] = new Node(u, adjList[vNum]);
}

void Graph::display() {
    cout << "vertex size: " << size << endl;
    for(int i = 0; i<MAX_VERTICES; i++) {
        if (vertices[i] == -1) continue;

        cout << vertices[i] << " : ";
        Node* head = adjList[i];
        while (head != NULL) {
            cout << vertices[convertToInt(head->getName())] << " ";
            head = head->getLink();
        }
        cout << endl;
    }
}