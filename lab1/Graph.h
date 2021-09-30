//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H
#include <vector>

using namespace std;

class Node {
private:
    string name;
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
    int size; // number of vertices

public:
    vector<Node*> vertices;
    vector<vector<Node*>> adjList;

    Graph();
    int getVerticesSize();
    int convertToOrder(string name);
    void insertVertex(string name, int xPos, int yPos);
    string getVertexName(int idx);
    void insertEdge(string start, string end);
    void createAdjList(vector<Node*> parsed);
    void display();

    // for the algorithms
    virtual vector<string> runAlgorithm(string start, string end, int startDepth) = 0;
};

#endif //AI_LABS_GRAPH_H