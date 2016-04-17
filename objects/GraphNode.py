'''
Created on Apr 14, 2016

@author: chunq
'''

class GraphNode(object):
    '''
    a single Graph node that makes up a graph object
    '''
    def __init__(self, data, neighbors = []):
        '''
        Constructor
        '''
        self.data = data
        self.neighbors = neighbors
        self.visited = False
        return   
    
    def append(self, nextNeighbor):
        self.neighbors.append(nextNeighbor)