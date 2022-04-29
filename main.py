#import numpy as np
import pandas as pd
import csv

class Graph:

    def __init__(self, V):

        self.V = V #Vertices
        self.adj = [[] for i in range(self.V)] #adjency lists
        self.Time = 0
        self.b_count = 0

    def NumberOfconnectedComponents(self):

        #mark all the vertices as not visited
        visited = [False for i in range(self.V)]

        #nb of connected components counter
        count = 1

        #explore the component if its not visited already
        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited)
                count+=1
        return count

    def dfs(self, v, visited):
        #mark the current node as visited
        visited[v] = True

        #visit the nodes one by one
        for i in self.adj[v]:
            if not visited[i]:
                self.dfs(i, visited)    
    
    def addEdge(self, v, w):
        if w not in self.adj[v] and v not in self.adj[w]: #gestion des doublons
            self.adj[v].append(w)
            self.adj[w].append(v)

    def G4G_bridgeUtil(self,u, visited, parent, low, disc): 
    
            # Mark the current node as visited and print it 
            visited[u]= True
    
            # Initialize discovery time and low value 
            disc[u] = self.Time 
            low[u] = self.Time 
            self.Time += 1
    
            #Recur for all the vertices adjacent to this vertex 
            for v in self.adj[u]: 
                # If v is not visited yet, then make it a child of u 
                # in DFS tree and recur for it 
                if visited[v] == False : 
                    parent[v] = u 
                    self.G4G_bridgeUtil(v, visited, parent, low, disc) 
    
                    # Check if the subtree rooted with v has a connection to 
                    # one of the ancestors of u 
                    low[u] = min(low[u], low[v]) 
    
    
                    ''' If the lowest vertex reachable from subtree 
                    under v is below u in DFS tree, then u-v is 
                    a bridge'''
                    if low[v] > disc[u]: 
                        #print ("%d %d" %(u,v)) 
                        self.b_count+=1
        
                        
                elif v != parent[u]: # Update low value of u for parent function calls. 
                    low[u] = min(low[u], disc[v]) 
    
    # DFS based function to find all bridges. It uses recursive 
    # function bridgeUtil() 
    def G4G_bridge(self): 

        # Mark all the vertices as not visited and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 

        # Call the recursive helper function to find bridges 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if visited[i] == False: 
                self.G4G_bridgeUtil(i, visited, parent, low, disc) 
        
        return self.b_count

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


    return (G.NumberOfconnectedComponents(), G.G4G_bridge(), 0)  # replace with your own code


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





