'''
Created on Apr 17, 2016

@author: chunq
'''

class TreeNode(object):
    '''
    Tree Node with 2 children at most
    '''


    def __init__(self, data):
        '''
        Constructor
        '''
        self.data = data
        self.left = None
        self.right = None
        return
    
    def __repr__(self, level = 0):
        ret = "\t" * level + repr(self.data) + "\n"
        if self.left is not None:
            ret += self.left.__repr__(level + 1)
        elif self.right is not None:
            ret += self.right.__repr__(level + 1)
        return ret  
    
    def setLeft(self, left = None):
        self.left = left
        return
    
    def setRight(self, right = None):
        self.right = right
        return
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right