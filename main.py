import sys
import pandas as pd
import csv
from collections import defaultdict
sys.setrecursionlimit(2000)


class Graph:

    def __init__(self, V):

        self.V = V #Vertices
        self.adj = defaultdict(list)
        self.Time = 0
        self.bridges = 0
        self.bridges_list = []
        self.components = 1
        self.component_id = [self.V]
        self.connected_components = []
        self.edges = []

    def FindConnectedComponents(self):
        self.connected_components = []

        #mark all the vertices as not visited
        visited = [False for i in range(self.V)]

        self.component_id = [-1 for i in range(self.V)]

        #explore the component if its not visited already
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                self.connected_components.append(self.dfs(temp, v, visited))
        return self.connected_components

    def dfs(self, temp, v, visited):
        #if visited[v]: return #node already visted
        #mark the current node as visited
        visited[v] = True
        #self.component_id[v] = currentComponentID
        temp.append(v)

        #visit the nodes one by one
        for w in self.adj[v]:
            if visited[w] == False:
                temp = self.dfs(temp, w, visited)
        return temp
    
    def isConnected(self, v, w):
        for component in self.connected_components:
            if v in component:
                if w not in component: 
                    return False
                elif w in component:
                    return True

        return False

    def addEdge(self, v, w):
        if w not in self.adj[v] and v not in self.adj[w] and v!=w: #gestion des doublons
            self.adj[v].append(w)
            self.adj[w].append(v)
            self.edges.append([v, w])
    def removeEdge(self, v, w):
        if v in self.adj[w] and w in self.adj[v]:
            self.adj[v].remove(w)
            self.adj[w].remove(v)
            self.edges.remove([v, w])


    def bridge(self): #naive implementation with connected components
        tried_bridges = []
        for v in range(0, self.V):
            for w in self.adj[v]:
                if [v, w] in tried_bridges or [w, v] in tried_bridges:
                    print("Edge ["+str(v)+"-"+str(w)+"] has already been visited")
                    print(tried_bridges)
                    continue
                tried_bridges.append([v, w])
                print("trying edge ["+str(v)+"-"+str(w)+"]")
                
                self.FindConnectedComponents()
                self.removeEdge(v, w)
                self.FindConnectedComponents()
                if not self.isConnected(v, w): #if after removal, they can't reach each other, then it's a bridge
                    self.bridges_list.append([v, w])
                    self.bridges+=1
                    print("["+str(v)+"-"+str(w)+"] is a bridge ! Bridges so far: "+ str(self.bridges))
                self.addEdge(v, w)

        return self.bridges

    def isBridge(self, visited, current, a, b):
        visited[current] = True
        print(visited[current])
        for w in self.adj[current]:
            if visited[w] or (w == a and b == current):
                continue
            else:
                print("statement 1")
                if w == a:
                    
                    return False
                if not self.isBridge(visited, w, a, b):
                    return False
        return True


    def isBridge2(self, v, w):
        cc = len(self.FindConnectedComponents())
        self.removeEdge(v, w)
        new_cc = len(self.FindConnectedComponents())
        if(cc != new_cc): 
            self.addEdge(v, w)
            return True
        else: 
            self.addEdge(v, w)
            return False


    def findBridges(self):
        self.bridges_list = []
        visited = []
        print(len(self.edges))
        for edge in self.edges:
            v, w = edge[0], edge[1]
            if [v,w] in visited or [w, v] in visited: 
                print("["+str(v)+"-"+str(w)+"] has already been visited")
                continue
            
            if self.isBridge2(v, w):
                print("["+str(v)+"-"+str(w)+"] is a Bridge")
                self.bridges_list.append([v, w])
            else:
                print("["+str(v)+"-"+str(w)+"] is not a Bridge")
            visited.append([v, w])
        return self.bridges_list

def getUndirectedGraphFromDataframe(df):
    G = Graph(35591) #create new graph instance with number of Non empty rows as vertices number
    for row in df.itertuples():
        G.addEdge(row[1], row[2]) #add edge from source to target
    print(len(G.edges))
    return G

def basic_properties(df):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: (number_of_different_components, number_of_bridges, number_of_local_bridges)
    """
    G = getUndirectedGraphFromDataframe(df)
    G.findBridges()


    return (len(G.FindConnectedComponents())+1, len(G.bridges_list), 0)  # replace with your own code


def total_triadic_closures(df):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: Returns the total amount of triadic closures that arrise between the median timestamp of the dataframe until the last timestamp.
    Reminder: The triadic closures do not take into account the sign of the edges.
    """
    return 0  # replace with your own code


def end_balanced_degree(dataframe):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: Returns the final balance degree of the graph (as defined in the project statement).
    Reminder: Take into account that the graph is weighted now.
    """
    return 0  # replace with your own code


def distances(dataframe):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: Returns a list where the element at index i represents the total number of small paths of distances i+1 in the graph.
    Reminder: Take into account that the graph is directed now.
    """
    return [0, 0, 0, 0, 0]  # replace with your own code


def pagerank(dataframe):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: (index, pagerank_value)
    where the index represents the id of the node with the highest pagerank value and pagerank_value its associated pagerank value after convergence.
    (we consider that we reached convergence when the sum of the updates on all nodes after one iteration of PageRank is smaller than 10^(-10))
    Reminder: Take into account that the graph is directed now.
    """
    return (0, 0.0)  # replace with your own code

if __name__ == "__main__":
    df = pd.read_csv('data.csv')
    df.head()

    print("TASK 1")
    print("Number of components: ", basic_properties(df)[0])
    print("Number of bridges: ", basic_properties(df)[1])
    print("Number of local bridges: ", basic_properties(df)[2])