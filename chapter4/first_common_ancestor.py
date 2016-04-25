'''
Created on Apr 24, 2016

First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 

@author: chunq
'''

def getFirstCommonAncestor(tree, descendant1, descendant2):
    return getFirstCommonAncestorHelper(tree.root, descendant1, descendant2)

def isAncestor(ancestorNode, descendant):
    if ancestorNode is None:
        return False
    if ancestorNode is descendant:
        return True
    return isAncestor(ancestorNode.left, descendant) or isAncestor(ancestorNode.right, descendant)

def getFirstCommonAncestorHelper(ancestorNode, descendant1, descendant2):
    if ancestorNode is None:
        return None
    elif isAncestor(ancestorNode.left, descendant1) and isAncestor(ancestorNode.left, descendant2):
        return getFirstCommonAncestorHelper(ancestorNode.left, descendant1, descendant2)
    elif isAncestor(ancestorNode.right, descendant1) and isAncestor(ancestorNode.right, descendant2):
        return getFirstCommonAncestorHelper(ancestorNode.right, descendant1, descendant2)
    else:
        return ancestorNode

if __name__ == '__main__':
    from objects.BSTNode import BST
    testTree = BST()
    testTree.insert(5)
    testTree.insert(2)
    testTree.insert(3)
    testTree.insert(7)
    testTree.insert(1)
    testTree.insert(4)
    testTree.insert(9)
    testTree.insert(8)
    print(testTree)
    node4 = testTree.find(4)
    node3 = testTree.find(3)
    print(getFirstCommonAncestor(testTree, node4, node3))
