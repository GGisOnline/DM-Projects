import sys
import pandas as pd
import csv
sys.setrecursionlimit(1000)


class Graph:

    def __init__(self, V):

        self.V = V #Vertices
        self.adj = [[] for i in range(self.V)] #adjency lists
        self.Time = 0
        self.bridges = 0
        self.components = 1
        self.component_id = [self.V]


        self.low = [self.V]
        self.pre = [self.V]
        cnt=0

    def FindConnectedComponents(self):

        #mark all the vertices as not visited
        visited = [False for i in range(self.V)]

        self.component_id = [-1 for i in range(self.V)]

        currentComponentID = 0

        #explore the component if its not visited already
        for v in range(self.V):
            if not visited[v]:
                currentComponentID = currentComponentID+1
                self.dfs(v, visited, currentComponentID)
                self.components+=1
        return self.component_id

    def dfs(self, v, visited, currentComponentID):
        #if visited[v]: return #node already visted
        #mark the current node as visited
        visited[v] = True
        self.component_id[v] = currentComponentID

        #visit the nodes one by one
        for w in self.adj[v]:
            if not visited[w]:
                self.dfs(w, visited, currentComponentID)    
    
    def isConnected(self, v, w):
        return self.component_id[v] == self.component_id[w]

    def addEdge(self, v, w):
        if w not in self.adj[v] and v not in self.adj[w] and v!=w: #gestion des doublons
            self.adj[v].append(w)
            self.adj[w].append(v)
    def removeEdge(self, v, w):
        if w in self.adj[w] and w in self.adj[v]:
            self.adj[v].remove(w)
            self.adj[w].remove(v)

    def bridge(self): #naive implementation with connected components
        #print("adjency list of 13 "+ str(self.adj[13]))
        for v in range(0, self.V):
            for w in self.adj[v]:
                #print("removing edge "+str(v)+"-"+str(w))
                self.removeEdge(v, w)
                self.FindConnectedComponents()
                if not self.isConnected(v, w): #if after removal, they can't reach each other, then it's a bridge
                    self.bridges+=1
                    print("Bridge Found between "+str(v)+"-"+str(w))
                    print("number of bridges so far: "+ str(self.bridges))
                self.addEdge(v, w)
                #print("re-adding edge "+str(v)+"-"+str(w))

def getUndirectedGraphFromDataframe(df):
    G = Graph(35591) #create new graph instance with number of Non empty rows as vertices number
    for row in df.itertuples():
        G.addEdge(row[1], row[2]) #add edge from source to target
    
    return G


def basic_properties(df):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: (number_of_different_components, number_of_bridges, number_of_local_bridges)
    """
    G = getUndirectedGraphFromDataframe(df)
    G.FindConnectedComponents()


    return (G.components, G.bridge(), 0)  # replace with your own code


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





