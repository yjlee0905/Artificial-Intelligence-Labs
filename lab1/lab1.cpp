#include <iostream>
#include <unistd.h>
#include <fstream>
#include <vector>
#include "Graph.h"
#include "BFS.h"
#include "IterativeDeepeningSearch.h"
#include "Astar.h"

using namespace std;

void readFileAndInit(string filename);
vector<string> split(string target, string delim);

vector<Node*> parsedVertices;
vector<pair<string, string>> parsedEdges;

Graph* g;

int main(int argc, char* argv[]) {
    int c;
    char algorithm;
    string startNode;
    string endNode;
    bool isV = false;
    int initialDepth = -1;

    while ((c = getopt(argc, argv, "s:e:a:d:v")) != -1) {
        switch (c) {
            case 'a':
                sscanf(optarg, "%c", &algorithm);
                break;
            case 's':
                for(; *optarg != '\0'; optarg++) {
                    startNode += *optarg;
                }
                break;
            case 'e':
                for(; *optarg != '\0'; optarg++) {
                    endNode += *optarg;
                }
                break;
            case 'v':
                isV = true;
                break;
            case 'd':
                sscanf(optarg, "%d", &initialDepth);
                break;
            default:
                cout << c << " is unsupported option in this program." << endl;
                exit(1);
        }
    }

    switch (algorithm) {
        case 'B':
            g = new BFS();
            break;
        case 'I':
            g = new IterativeDeepeningSearch();
            break;
        case 'A':
            g = new Astar();
            break;
    }

    string fileName = argv[optind];

    // Read file and save vertices, edges
    //readFileAndInit("/Users/yjeonlee/Desktop/[Fall2021]AI/AI_Labs/lab1/inputs/ex2.txt");
    readFileAndInit(fileName);

    vector<string> finalPath = g->runAlgorithm(startNode, endNode, initialDepth, isV);
    if (finalPath.size() > 0) {
        cout << "Solution:";
        for (int i = 0; i < finalPath.size(); i++) {
            if (i == finalPath.size()-1) {
                cout << " " << finalPath.at(i);
            } else {
                cout << " " << finalPath.at(i) << " ->";
            }
        }
    }
    cout << endl;

    return 0;
}

void readFileAndInit(string filename) {
    ifstream in;
    in.open(filename);
    if (!in) {
        cerr << "Cannot open file!" << endl;
        exit(1);
    }

    vector<string> parsed;
    const char delim[] = " ";
    string line;
    while (getline(in, line)) {
        if (line.find("#") == 0 || line.size() == 0) continue;
        //cout << line << endl;
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
        g->insertVertex(parsedVertices.at(i)->getName(), parsedVertices.at(i)->getXpos(), parsedVertices.at(i)->getYpos());
    }

    // Insert Edges;
    g->createAdjList(parsedVertices);

    for (int i = 0; i < parsedEdges.size(); ++i) {
        g->insertEdge(parsedEdges.at(i).first, parsedEdges.at(i).second);
    }
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
    //const char whiteSpaces[] = " \t\r\n\v\g";
    //target.erase(remove(target.begin(), target.end(), whiteSpaces), target.end());
    if (target.length() > 0) {
        splited.push_back(target);
    }
    return splited;
}