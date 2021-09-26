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

void Graph::insertVertex(string name, int xPos, int yPos) {
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

    // TODO ordering? to be removed because adjList
//    Node* newNode = new Node(name, xPos, yPos);
//    vector<Node*> adjList;
//    adjList.push_back(newNode);
//    graph.push_back(adjList);
    size++;
}

string Graph::getVertex(int idx) {
    return vertices.at(idx);
}

void Graph::insertEdge(string start, string end) {
    int startOrder = convertToOrder(start);
    int endOrder = convertToOrder(end);
    cout << "u: " << start << "  uNums: " << startOrder << "     v: " << end << "  endOrder: " << endOrder << endl;

    // insert to start adjList
    int targetIdx = -1;
    for (int i=1; i<adjList[startOrder].size(); i++) {
        if (end.compare(adjList[startOrder].at(i)->getName()) < 0) {
            targetIdx = i;
            break;
        }
    }

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


//    adjList[startOrder] = new Node(v, adjList[startOrder]);
//    adjList[endOrder] = new Node(u, adjList[endOrder]);
    // TODO 여기서 각자의 list에 대해 sorting 진행
}

void Graph::createAdjList(vector<Node*> parsed) {
    for (int i=0; i<vertices.size(); i++) {
        int x, y;
        for (int j = 0; j < parsed.size(); ++j) {
            if (vertices.at(i).compare(parsed.at(j)->getName()) == 0) {
                x = parsed.at(j)->getXpos();
                y = parsed.at(j)->getYpos();
                break;
            }
        }

        vector<Node*> nodeList;
        Node* startNode = new Node(vertices.at(i), x, y);
        nodeList.push_back(startNode);
        adjList.push_back(nodeList);
    }
    cout << "adjList size: " << adjList.size() << endl;
}

//void Graph::insertInLinkedList(Node *head, Node *newNode) {
//   if (head->getLink() == NULL) {
//        head->setLink(newNode);
//    } else {
//
//    }
//}


Node* Graph::getAdjListNode(int idx) {
    //return adjList[idx];
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
//    cout << "vertex size: " << size << endl;
//    for(int i = 0; i<MAX_VERTICES; i++) {
//        if (vertices[i].compare("") == 0) continue;
//
//        cout << vertices[i] << " : ";
//        Node* head = adjList[i];
//        while (head != NULL) {
//            cout << vertices[convertToOrder(head->getName())] << " ";
//            head = head->getLink();
//        }
//        cout << endl;
//    }
}