'''
Paths with Sum: You are given a binary tree in which each node contains an integer value
(which might be positive or negative). Design an algorithm to count the number of paths 
that sum to a given value. The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).
'''

def getPathsWithSum(bst, targetSum):
	result = []
	if bst.root:
		getPathsWithSumHelper(bst.root, targetSum, 0, [], result)
	if len(result)>0:
		print(result)
	else:
		print("No path found.")
	return

def getPathsWithSumHelper(node, targetSum, currentSum, paths, result):
	if node is None:
		return
	paths.append(node)
	currentSum += node.key
	if currentSum == targetSum:
		result.append(paths)
	getPathsWithSumHelper(node.left, targetSum, currentSum, paths[:], result)
	getPathsWithSumHelper(node.right, targetSum, currentSum, paths[:], result)
	return

if __name__ == '__main__':
	from objects.BST import BST
	testTree = BST()
	testTree.insert(4)
	testTree.insert(-2)
	testTree.insert(2)
	testTree.insert(1)
	testTree.insert(-3)
	testTree.insert(3)
	print(testTree)
	getPathsWithSum(testTree,5)
