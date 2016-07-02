"""
Given a directed graph, design an algorithm to find out whether there is a route 
between two nodes.
"""

from Graph import *

def find_path2(g, start_node, end_node):
    """
    This requires a simple graph traversal using either depth-first search 
    or breadth-first search. Breadth-first search is likely to be quicker and 
    is likely to provide the shortest path.
    """
    
    
    return False       

g = Graph(True)
v_a = g.insert_vertex('a')
v_b = g.insert_vertex('b')
v_b = g.insert_vertex('c')

g.insert_edge(v_a, v_b, 'a->b')
e_ab = g.get_edge(v_a, v_b)
print e_ab._element
