'''
Created on Apr 14, 2016

@author: chunq
'''

from collections import deque

class Graph(object):
    '''
    Graph object
    '''

    def __init__(self, root = None):
        '''
        Constructor
        '''
        self.root = root
        self.count = 0
    
    def traverseDFS(self):
        '''
        DFS
        '''
        self._visitDFS(self.root)
    
    def _visitDFS(self, currentNode):
        '''
        DFS helper function
        '''
        if (currentNode is None) or (currentNode.visited == True):
            return
        else:
            print(currentNode.data)
            currentNode.visited = True
            for neighbor in currentNode.neighbors:
                self._visit(neighbor)
            return
    
    def traverseBFS(self):
        '''
        BFS
        '''
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            currentNode = queue.popleft()
            print(currentNode.data)
            currentNode.visited = True
            for neighbor in currentNode.neighbors:
                if neighbor.visited == False:
                    neighbor.visited = True
                    queue.append(neighbor)