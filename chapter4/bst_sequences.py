'''
Created on Apr 24, 2016

BST Sequences: A binary search tree was created by traversing through an array from left to right and inserting 
each element. Given a binary search tree with distinct elements, print all possible arrays that could have led to 
this tree.

@author: chunq
'''

def getBSTSequences(tree):
    result = []
    getBSTSequncesHelper(tree.root, result)
    return result

def getBSTSequncesHelper(node, result):
    if node is None:
        result.append([])
        return
    leftResult = []
    rightResult = []
    getBSTSequncesHelper(node.left, leftResult)
    getBSTSequncesHelper(node.right, rightResult)
    for left in leftResult:
        for right in rightResult:
            temp = []
            weave(left, right, [], temp)
            for one in temp:
                result.append(one)
    for oneResult in result:
        oneResult.insert(0, node)       

def weave(list1, list2, prehend, result):
    if (len(list1) == 0) or (len(list2) == 0):
        result.append(prehend + list1 + list2)
        return
    if len(list1) > 0:
        prehend.append(list1[0])
        weave(list1[1:], list2, prehend, result)
        prehend.pop()
    if len(list2) > 0:
        prehend.append(list2[0])
        weave(list1, list2[1:], prehend, result)
        prehend.pop()

if __name__ == '__main__':
    from objects.BSTNode import BST
    testTree = BST()
    testTree.insert(5)
    testTree.insert(2)
    testTree.insert(6)
    print(getBSTSequences(testTree))