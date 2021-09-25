//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H
#include <vector>

using namespace std;

// TODO check max vertices
const int MAX_VERTICES = 1024;

class Node {
private:
    string name; // TODO check name is char or string
    // int order;
    int xPos;
    int yPos;
    Node* link;

public:
    Node(string name, Node* link);
    //Node(char name, int xPos, int yPos, Node* link);
    void setLink(Node* link);
    Node* getLink();
    string getName();
};

class Graph {
private:
    int size; // 정점의 개수
    vector<string> vertices; // 정점의 이름
    Node* adjList[MAX_VERTICES]; // 인접 리스트

    void insertInLinkedList(Node* head, Node* newNode);

public:
    Graph();
    int convertToOrder(string name);
    void insertVertex(string name);
    string getVertex(int idx);
    void insertEdge(string u, string v);
    Node* getAdjListNode(int idx);
    void display();
};

#endif //AI_LABS_GRAPH_H