#include <iostream>
#include "Graph.h"

using namespace std;

int main() {
    Graph g;

    g.insertVertex('A');
    g.insertVertex('B');
    g.insertVertex('C');
    g.insertVertex('D');

    g.insertEdge('A', 'B');
    g.insertEdge('A', 'C');
    g.insertEdge('A', 'D');
    g.insertEdge('C', 'D');

    g.display();
    return 0;
}
