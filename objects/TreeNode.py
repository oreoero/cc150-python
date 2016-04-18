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
    
    def __repr__(self, level = 0, left = False):
        if level == 0:
            ret = 'root: ' + str(self.data) + "\n"
        else:
            if left:
                ret = "\t" * level + 'left: ' + str(self.data) + "\n"
            else:
                ret = "\t" * level + 'right: ' + str(self.data) + "\n"
                
        if self.left is not None:
            ret += self.left.__repr__(level + 1, True)
        if self.right is not None:
            ret += self.right.__repr__(level + 1)
        return ret  