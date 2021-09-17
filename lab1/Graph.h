//
// Created by Yunjeon Lee on 2021/09/17.
//

#ifndef AI_LABS_GRAPH_H
#define AI_LABS_GRAPH_H

class Node {
private:
    char name; // TODO check name is char or string
    int xPos;
    int yPos;
    Node* link;
public:
    Node(char name, int Xpos, int Ypos, Node* link);
};

class Graph {

};

#endif //AI_LABS_GRAPH_H