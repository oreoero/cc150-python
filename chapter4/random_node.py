'''
Random Node: You are implementing a binary search tree class from scratch, which in addition
to insert, find, and delete, has a method getRandomNode() which returns a random node from 
the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods
'''

from objects.BST import BSTNode
from random import randint

class RandomBST(object):
	def __init__(self):
		self.root = None
		self.count = 0

	def getRandomNode(self):
		prob = randint(0, 99) / 100 * self.count
		if self.root:
			return self.root.getRandomNode(prob)
		else:
			return None

	def insert(self, key):
		if self.root:
			self.root.insert(key)
		else:
			newNode = RandomBSTNode(key)
			self.root = newNode
		self.count += 1

	def find(self, key):
		pass

	def delete(self, key):
		pass


class RandomBSTNode (BSTNode):
	def __init__(self, key):
		super().__init__(key)
		self.count = 1

	def getRandomNode(self, prob):
		if self is None:
			return None

		leftTotal = self.left.count if self.left else 0
		rightTotal = self.right.count if self.right else 0
		total = leftTotal + rightTotal + 1

		if prob < 1:
			return self
		elif prob < 1 + leftTotal:
			return self.left.getRandomNode(prob / total * (total - 1 - rightTotal))
		else:
			return self.right.getRandomNode(prob / total * (total - 1 - leftTotal))

	def insert(self, key):
		if self.key == key:
			return
		elif self.key < key:
			if self.right:
				self.right.insert(key)
			else:
				newNode = RandomBSTNode(key)
				newNode.parent = self
				self.right = newNode
		else:
			if self.left:
				self.left.insert(key)
			else:
				newNode = RandomBSTNode(key)
				newNode.parent = self
				self.left = newNode
		self.count += 1

	def find(self, key):
		pass

	def delete(self):
		pass

if __name__ == '__main__':
	testTree = RandomBST()
	testTree.insert(2)
	testTree.insert(1)
	testTree.insert(6)
	testTree.insert(4)
	testTree.insert(5)
	testTree.insert(15)
	testTree.insert(25)
	testTree.insert(35)
	testTree.insert(3)
	print(testTree.getRandomNode())