'''
Created on Apr 21, 2016

Validate BST: Implement a function to check if a binary tree is a binary search tree

@author: chunq
'''

from objects.BSTNode import BST
import sys

def validateBST(tree):
    if tree.root is None:
        return False
    return validateBSTHelper(tree.root, -sys.maxsize-1, sys.maxsize)

def validateBSTHelper(node, low, high):
    if node is None:
        return True
    if not ((node.key >= low) and (node.key <= high)):
        return False
    else:
        return validateBSTHelper(node.left, -sys.maxsize-1, node.key) and \
            validateBSTHelper(node.right, node.key, sys.maxsize)
    
if __name__ == '__main__':
    testTree = BST()
    testTree.insert(5)
    testTree.insert(2)
    testTree.insert(3)
    testTree.insert(7)
    testTree.insert(1)
    testTree.insert(4)
    testTree.insert(9)
    testTree.insert(8)
    testTree.root.key = -1
    print(testTree)
    print(validateBST(testTree))