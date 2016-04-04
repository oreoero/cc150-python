'''
Created on Mar 30, 2016

@author: chunq
'''

from objects.LinkedList import LinkedList
from objects.LinkedNode import LinkedNode

class AdvancedLinkedList(LinkedList):
	def removeDuplicate(self):
		node = self.head
		prev = self.head
		tempList = []
		while node is not None:
			if node.data in tempList:
				prev.next = node.next
			else:
				tempList.append(node.data)
			prev = node
			node = node.next
		return
	
if __name__ == "__main__":
	testList = AdvancedLinkedList()
	testList.append(LinkedNode(4))
	testList.append(LinkedNode(4))
	testList.removeDuplicate()
	testList.view()
			
		