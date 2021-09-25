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

Node::Node(string name, Node *link) {
    this->name = name;
    this->link = link;
}

void Node::setLink(Node *link) {
    this->link = link;
}

Node* Node::getLink() {
    return link;
}

string Node::getName() {
    return name;
}

Graph::Graph() {
    this->size = 0;
    // initialize vertices
    for (int i = 0; i < vertices.size(); i++) {
        vertices.at(i) = ""; // TODO check later
    }
}

int Graph::convertToOrder(string name) {
    //return name - 'A';
    for (int i = 0; i < vertices.size(); i++) {
        if (vertices[i].compare(name) == 0) {
            return i;
        }
    }
}

void Graph::insertVertex(string name) {
    int targetIdx = -1;
    for (int i = 0;  i < vertices.size(); i++) {
        if (name.compare(vertices.at(i)) < 0) {
            targetIdx = i;
            break;
        }
    }

    if (targetIdx != -1) {
        vertices.insert(vertices.begin() + targetIdx, name);
    } else {
        vertices.push_back(name);
    }
    // TODO Graph validation check : graph full?
    adjList[convertToOrder(name)] = NULL;
    size++;
}

string Graph::getVertex(int idx) {
    return vertices.at(idx);
}


void Graph::insertEdge(string u, string v) {
    int uNum = convertToOrder(u);
    int vNum = convertToOrder(v);
    cout << "u: " << u << "  uNums: " << uNum << "     v: " << v << "  vNum: " << vNum << endl;

    adjList[uNum] = new Node(v, adjList[uNum]);
    adjList[vNum] = new Node(u, adjList[vNum]);
    // TODO 여기서 각자의 list에 대해 sorting 진행
}

void Graph::insertInLinkedList(Node *head, Node *newNode) {
    if (head->getLink() == NULL) {
        head->setLink(newNode);
    } else {

    }
}


Node* Graph::getAdjListNode(int idx) {
    return adjList[idx];
}

void Graph::display() {
    cout << "vertex size: " << size << endl;
    for(int i = 0; i<MAX_VERTICES; i++) {
        if (vertices[i].compare("") == 0) continue;

        cout << vertices[i] << " : ";
        Node* head = adjList[i];
        while (head != NULL) {
            cout << vertices[convertToOrder(head->getName())] << " ";
            head = head->getLink();
        }
        cout << endl;
    }
}