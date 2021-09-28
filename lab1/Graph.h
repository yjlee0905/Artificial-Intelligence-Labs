//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H
#include <vector>

using namespace std;

class Node {
private:
    string name; // TODO check name is char or string
    int xPos;
    int yPos;

public:
    Node(string name, int xPos, int yPos);
    string getName();
    int getXpos();
    int getYpos();
};

class Graph {
private:
    int size; // 정점의 개수

public:
    vector<Node*> vertices; // 정점의 이름
    vector<vector<Node*>> adjList; // 인접 리스트

    Graph();
    int getVerticesSize();
    int convertToOrder(string name);
    void insertVertex(string name, int xPos, int yPos);
    string getVertexName(int idx);
    void insertEdge(string start, string end);
    void createAdjList(vector<Node*> parsed);
    void display();
};

#endif //AI_LABS_GRAPH_H