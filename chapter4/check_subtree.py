'''
Created on Apr 24, 2016

Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to
determine if T2 is a subtree of T1

A tree T2 is a subtree of T1 if there exits a node n in T1 such that the sub tree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.

@author: chunq
'''

from objects.BST import BST

def isSubTree(T1, T2):
	return isSubTreeHelper(T1.root, T2)

def isSubTreeHelper(node, T2):
	if node is None:
		return False
	if isIdentical(node, T2.root):
		return True
	return isSubTreeHelper(node.left, T2) or isSubTreeHelper(node.right, T2)

def isIdentical(node1, node2):
	if node1 and node2:
		return True
	if node1 is None or node2 is None:
		return False
	if node1.key != node2.key:
		return False
	return isIdentical(node1.left, node2.left) and isIdentical(node1.right, node2.right)


if __name__ == '__main__':
    testT1 = BST()
    testT1.insert(1)
    testT1.insert(2)
    print(testT1)
    print()
    testT2 = BST()
    testT2.insert(2)
    print(testT2)
    print(isSubTree(testT1, testT2))
