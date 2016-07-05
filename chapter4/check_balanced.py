'''
Created on Apr 21, 2016

Check Balanced: Implement a function to check if a binary tree is balanced. For the 
purpose of this question, a balanced tree is defined to be a tree such that the heights
of the two subtrees of any node never differ by more than one.

@author: chunq
'''

def isBalanced(tree):
    return (getHeight(tree.root) != -1)

def getHeight(node):
    if node is None:
        return 0
    leftHeight = getHeight(node.left)
    if leftHeight == -1:
        return -1
    rightHeight = getHeight(node.right)
    if rightHeight == -1:
        return -1
    if abs(rightHeight - leftHeight) > 1:
        return -1
    return max(rightHeight, leftHeight) + 1
    
if __name__ == '__main__':    
    from objects.BST import BST
    testTree = BST()
    testTree.insert(5)
    testTree.insert(3)
    testTree.insert(7)
    testTree.insert(1)
    testTree.insert(4)
    testTree.insert(9)
    testTree.insert(8)
    print(testTree)
    print(isBalanced(testTree))