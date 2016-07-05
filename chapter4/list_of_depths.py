'''
Created on Apr 21, 2016

List of Depths: Given a binary tree, design an algorithm which creates a linked list of all 
the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked list).

@author: chunq
'''

def listOfDepths(tree):
    result = []
    listOfDepthsHelper(tree.root, 0, result)
    return result

def listOfDepthsHelper(node, level, result):
    if len(result) == level:
        result.append([])
    result[level].append(node.key)
    if node.left:
        listOfDepthsHelper(node.left, level + 1, result)
    if node.right:
        listOfDepthsHelper(node.right, level + 1, result)

def listOfDepthsBFS(tree):
    result = []
    newLevel = []
    previousLevel = []
    if tree.root:
        newLevel.append(tree.root)
    while len(newLevel) > 0:
        result.append(newLevel)
        previousLevel = newLevel
        newLevel = []
        for node in previousLevel:
            if node.left:
                newLevel.append(node.left)
            if node.right:
                newLevel.append(node.right)
    return result
    
def test():
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
    print(listOfDepths(testTree))
    print(listOfDepthsBFS(testTree))
  
if __name__ == '__main__':
    test()