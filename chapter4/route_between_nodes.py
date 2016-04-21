'''
Created on Apr 17, 2016

Route Between Nodes: Given a directed graph, design an algorithem to find out
whether there is a route between two nodes

@author: chunq
'''

def routeBetweenNodes(source, destination):
    if source == destination:
        return True
    
def _visitDFS(node, target):
    if node is None or node.visited:
        return False
    node.visited = True
    hasFound = False
    for neighbor in node.neighbors:
        if neighbor == target:
            return True
        hasFound = _visitDFS(neighbor, target)
    return hasFound
    
    