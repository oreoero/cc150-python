'''
Created on Apr 20, 2016

Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

@author: chunq
'''

from objects.BST import BST

def minimalHeight(sortedList):
    tree = BST()
    minimalHeightBSTHelper(sortedList, tree, 0, len(sortedList) - 1)
    return tree    
    
def minimalHeightBSTHelper(sortedList, tree, lowIndex, highIndex):
    if lowIndex > highIndex:
        return
    midIndex = (lowIndex + highIndex) // 2
    tree.insert(sortedList[midIndex])
    minimalHeightBSTHelper(sortedList, tree, lowIndex, midIndex - 1)
    minimalHeightBSTHelper(sortedList, tree, midIndex + 1, highIndex)

def test():
    import random
    testList = sorted([random.randrange(100) for _ in range(int(7))])
    testTree = minimalHeight(testList)
    print(testTree)
    
if __name__ == '__main__':
    test()