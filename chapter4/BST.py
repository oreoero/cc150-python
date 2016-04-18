'''
Created on Apr 17, 2016

@author: chunq
'''

from objects.Tree import Tree
from objects.TreeNode import TreeNode

class BST(Tree):
    '''
    Binary Search Tree
    '''
    
    def insert(self, data):
        newNode = TreeNode(data)
        newNodeParent = None
        searchNode = self.root
        while searchNode is not None:
            newNodeParent = searchNode
            if data <= searchNode.data:
                searchNode = searchNode.left
            else:
                searchNode = searchNode.right
        if newNodeParent is None:
            self.root = newNode
        elif data <= newNodeParent.data:
            newNodeParent.left = newNode
        else:
            newNodeParent.right = newNode
    
    def find(self, target):
        return self._findHelper(self.root, target)
    
    def _findHelper(self, current, target):
        while current is not None:
            if current.data == target:
                return True
            elif target < current.data:
                return self._findHelper(current.left, target)
            else:
                return self._findHelper(current.right, target)
        return False
    

if __name__ == '__main__':
    testTree = BST()
    testTree.insert(2)
    testTree.insert(3)
    testTree.insert(1)
    print(testTree)
    print(testTree.find(2))
    print(testTree.find(1))
    print(testTree.find(4))
        
            
        