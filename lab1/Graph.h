//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H
#include <vector>

using namespace std;

// TODO check max parsedVertices
const int MAX_VERTICES = 1024;

class Node {
private:
    string name; // TODO check name is char or string
    int xPos;
    int yPos;
    // int order;
    //Node* link;

public:
    Node(string name, int xPos, int yPos);
    string getName();
    int getXpos();
    int getYpos();
    //Node(char name, int xPos, int yPos, Node* link);
    //void setLink(Node* link);
    //Node* getLink();
};

class Graph {
private:
    int size; // 정점의 개수
    vector<string> vertices; // 정점의 이름
    vector<vector<Node*>> adjList; // 인접 리스트
    //Node* adjList[MAX_VERTICES]; // 인접 리스트

public:
    Graph();
    int convertToOrder(string name);
    void insertVertex(string name, int xPos, int yPos);
    string getVertex(int idx);
    void insertEdge(string start, string end);
    void createAdjList(vector<Node*> parsed);
    Node* getAdjListNode(int idx);
    void display();
};

#endif //AI_LABS_GRAPH_H