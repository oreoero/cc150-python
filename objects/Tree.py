'''
Created on Apr 17, 2016

@author: chunq
'''

class Tree(object):
    '''
    Tree object
    '''

    def __init__(self, root = None):
        '''
        Constructor
        '''
        self.root = root
    
    def __repr__(self):
        return repr(self.root)