class LinkedList(object):
	def __init__(self):
		self.head = None
		self.count = 0
		return

	def find(self, node = None):
		if node is None:
			return True
		loop = self.head

		while loop is not None:
			if loop.data == node.data:
				return True
			else:
				loop = loop.next

		return False

	def remove(self, node = None):
		if node is None:
			return True

		loop = self.head
		prev = self.head

		while loop is not None:
			if loop.data == node.data:
				if loop == self.head:
					self.head = loop.next
				else:
					prev.next = loop.next

				self.count -= 1
				return True
			else:
				prev = loop
				loop = loop.next

		return False

	def append(self, node = None):
		node.next = self.head
		self.head = node
		self.count += 1
		return

	def view(self):
		loop = self.head
		print("Head:", end = ' ')

		while loop is not None:
			if loop.next is None:
				print(loop.data)
			else:
				print(loop.data, end = '=>')
			loop = loop.next

		print("Count:", self.count, end = ' ')

		return