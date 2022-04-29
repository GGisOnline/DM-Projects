from main import Graph

def test_1():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(0, 2)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    print("\nBridges in the graph are:", g.bridge())

if __name__ == "__main__":
    test_1()
    print("Everything passed")