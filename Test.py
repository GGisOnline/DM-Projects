from main import Graph

def test1():
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 0)
    print("connected components :")
    print(g.FindConnectedComponents())
    print("Are connected (2, 1) ? ", g.isConnected(2, 1))
    print("Are connected (2, 4) ? ", g.isConnected(2, 4))

def test_isBridge():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)

    print(g.isBridge2(0, 1))
    print(g.isBridge2(3, 4))
    print(g.isBridge2(2, 3))


def test2():

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.bridge2()
    print("\nBridges in the graph are:", g1.bridges)
    print()

def test_bridges_1():
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(0, 2)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.findBridges()

    print("\nBridges in the graph are:", str(g.bridges_list))
    print()

    g1 = Graph(5)
    g1.addEdge(1, 0)
    g1.addEdge(0, 2)
    g1.addEdge(2, 1)
    g1.addEdge(0, 3)
    g1.addEdge(3, 4)
    g1.findBridges()

    print("\nBridges in the graph are:", str(g1.bridges_list))
    print()

    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    g2.findBridges()
    print ("\nBridges in second graph ", str(g2.bridges_list))

    g3 = Graph (7)
    g3.addEdge(0, 1)
    g3.addEdge(1, 2)
    g3.addEdge(2, 0)
    g3.addEdge(1, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 6)
    g3.addEdge(3, 5)
    g3.addEdge(4, 5)
    g3.findBridges()
    print ("\nBridges in third graph ", str(g3.bridges_list))
    print()
        



if __name__ == "__main__":
    test_isBridge()
    print("Everything passed")