#include <iostream>
#include <fstream>
#include <vector>
#include "Graph.h"
#include "SearchAlgorithms.h"

using namespace std;

vector<string> split(string target, string delim);

vector<Node*> parsedVertices;
vector<pair<string, string>> parsedEdges;
SearchAlgorithms g;

int main() {
    // Read file and save vertices, edges
    ifstream in;
    in.open("/Users/yjeonlee/Desktop/[Fall2021]AI/AI_Labs/lab1/inputs/ex2.txt");
    if (!in) {
        cerr << "Cannot open file!" << endl;
        exit(1);
    }

    vector<string> parsed;
    const char delim[] = " ";
    string line;
    while (getline(in, line)) {
        if (line.find("#") == 0 || line.size() == 0) continue;
        cout << line << endl;
        parsed = split(line, delim);

        // Edge
        if (parsed.size() == 2) {
            pair<string, string> newEdge;
            newEdge.first = parsed.at(0);
            newEdge.second = parsed.at(1);
            parsedEdges.push_back(newEdge);
        }

        // Vertices
        if (parsed.size() == 3) {
            Node* newNode = new Node(parsed.at(0), stoi(parsed.at(1)), stoi(parsed.at(2)));
            parsedVertices.push_back(newNode);
        }
    }

    // Insert Vertices
    for (int i=0; i < parsedVertices.size(); i++) {
        g.insertVertex(parsedVertices.at(i)->getName(), parsedVertices.at(i)->getXpos(), parsedVertices.at(i)->getYpos());
    }

    // Insert Edges;
    g.createAdjList(parsedVertices);

    for (int i = 0; i < parsedEdges.size(); ++i) {
        g.insertEdge(parsedEdges.at(i).first, parsedEdges.at(i).second);
    }

    g.display();

    cout << "BFS" << endl;
    vector<string> res = g.BFS("S", "G");

    return 0;
}

vector<string> split(string target, string delim) {
    vector<string> splited;
    int pos = 0;
    string token;
    while ((pos = target.find(delim)) != std::string::npos) {
        token = target.substr(0, pos);
        splited.push_back(token);
        target.erase(0, pos + delim.length());
    }

    // TODO eliminate whitespaces
    //const char whiteSpaces[] = " \t\r\n\v\f";
    //target.erase(remove(target.begin(), target.end(), whiteSpaces), target.end());
    if (target.length() > 0) {
        splited.push_back(target);
    }
    return splited;
}