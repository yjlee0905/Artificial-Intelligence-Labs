//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H

// TODO check max vertices
const int MAX_VERTICES = 1024;

class Node {
private:
    char name; // TODO check name is char or string
    int xPos;
    int yPos;
    Node* link;

public:
    Node(char name, Node* link);
    //Node(char name, int xPos, int yPos, Node* link);
    void setLink(Node* link);
    Node* getLink();
    char getName();
};

class Graph {
private:
    int size;
    char vertices[MAX_VERTICES];
    Node* adjList[MAX_VERTICES];

    int convertToInt(char name);
    char convertToChar(int idx);

public:
    Graph();
    void insertVertex(char name);
    void insertEdge(char u, char v);
    void display();
};

#endif //AI_LABS_GRAPH_H