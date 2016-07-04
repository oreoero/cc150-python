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
    
    def insert(self, key):
        newNode = TreeNode(key)
        newNodeParent = None
        searchNode = self.root
        while searchNode:
            newNodeParent = searchNode
            if key == searchNode.key:
                return
            if key < searchNode.key:
                searchNode = searchNode.left
            else:
                searchNode = searchNode.right
        if newNodeParent is None:
            self.root = newNode
        elif key < newNodeParent.key:
            newNodeParent.left = newNode
        else:
            newNodeParent.right = newNode
    
    def find(self, target):
        return self._findHelper(self.root, target) == None
    
    def _findHelper(self, current, target):
        while current:
            if current.key == target:
                return current
            elif target < current.key:
                return self._findHelper(current.left, target)
            else:
                return self._findHelper(current.right, target)
        return None
    
    def delete(self, target):
        deleteNode = self.root
        deleteNodeParent = None
        while deleteNode:
            if deleteNode.key == target:
                break
            deleteNodeParent = deleteNode
            if target < deleteNode.key:
                deleteNode = deleteNode.left
            else:
                deleteNode = deleteNode.right
                
        if deleteNode.left is None or deleteNode.right is None:
            if deleteNodeParent.left is deleteNode:
                deleteNodeParent.left = deleteNode.left if deleteNode.right is None else deleteNode.right
            else:
                deleteNodeParent.right = deleteNode.left or deleteNode.right
        else:
            successorNode = deleteNode.right
            while successorNode.left:
                successorParentNode = successorNode
                successorNode = successorNode.left
            deleteNode.key = successorNode.key
            successorParentNode.left = successorNode.right
            
if __name__ == '__main__':
    '''
    Follow the example at: http://www.algolist.net/Data_structures/Binary_search_tree/Removal
    '''
    testTree = BST()
    testTree.insert(5)
    testTree.insert(2)
    testTree.insert(12)
    testTree.insert(-4)
    testTree.insert(3)
    testTree.insert(9)
    testTree.insert(21)
    testTree.insert(19)
    testTree.insert(20)
    testTree.insert(25)
    print(testTree)
    testTree.delete(12)
    print(testTree)
            
        