from main import Graph

def test_bridges_1():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(0, 2)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    print("\nBridges in the graph are:", g.bridge())

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    print("\nBridges in the graph are:", g1.bridge())

    g3 = Graph (7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    print ("\nBridges in third graph ", g3.bridge())

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print ("\nBridges in second graph ", g2.bridge())
    
        

if __name__ == "__main__":
    test_bridges_1()
    print("Everything passed")