#include <iostream>
#include "Graph.h"

using namespace std;

int main() {
    Graph g;

    g.insertVertex('S');
    g.insertVertex('Z');
    g.insertVertex('A');
    g.insertVertex('C');
    g.insertVertex('G');

    g.insertEdge('S', 'C');
    g.insertEdge('S', 'G');
    g.insertEdge('S', 'Z');
    g.insertEdge('C', 'A');
    g.insertEdge('Z', 'A');

    g.display();
    return 0;
}
