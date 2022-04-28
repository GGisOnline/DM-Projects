#import numpy as np
import pandas as pd
import csv
import graph as g


df = pd.read_csv('data.csv') #Si tu veux mettre le try/catch, c'est ici non?
df.head()


def getUndirectedGraphFromDataframe(df): 
    G = g(df.count())
    for row in df.itertuples():
        G.addEdge(row[1], row[2]) #add edge from source to target
    
    #todo: j'ai pas check les doublons du coup je sais pas si c'est bon
    return G


def basic_properties(df):
    """
    Input: Pandas dataframe as described above representing a graph
    Output: (number_of_different_components, number_of_bridges, number_of_local_bridges)
    """
    G = g.getUndirectedGraphFromDataframe(df)


    return (G.numberOfConnectedComponents(), 0, 0)  # replace with your own code


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



