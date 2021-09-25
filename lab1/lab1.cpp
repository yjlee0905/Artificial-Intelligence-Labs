#include <iostream>
#include "Graph.h"
#include "SearchAlgorithms.h"

using namespace std;

int main() {
    SearchAlgorithms g;

    g.insertVertex("S");
    g.insertVertex("A");
    g.insertVertex("C");
    g.insertVertex("B");
    g.insertVertex("E");
    g.insertVertex("D");
    g.insertVertex("G");

    g.insertEdge("S", "C");
    g.insertEdge("S", "A");
    g.insertEdge("A", "E");
    g.insertEdge("A", "C");
    g.insertEdge("A", "B");
    g.insertEdge("C", "D");
    g.insertEdge("D", "G");

    g.display();

    cout << "BFS" << endl;
    g.BFS("S");

    return 0;
}
