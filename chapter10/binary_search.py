'''
Binary search
'''

def binarySearch(list, target):
	pass

def binarySearchRecur(list, target):
	if len(list) == 0:
		return -1

	list = sorted(list)

	return binarySearchHelper(list, 0, len(list)-1, target)

def binarySearchHelper(list, start, end, target):
	if start > end:
		return -1
	mid = int((start + end) / 2)
	if list[mid] == target:
		return mid
	elif list[mid] < target:
		return binarySearchHelper(list, mid+1, end, target)
	else:
		return binarySearchHelper(list, start, mid-1, target)
	return -1

if __name__ == '__main__':
	list = [x for x in range(1, 9)]
	print(binarySearchRecur(list, 8))