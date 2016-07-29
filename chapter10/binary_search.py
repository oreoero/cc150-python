'''
Binary search
return the last occurrence
'''

def binarySearch(list, target):
	if len(list) == 0:
		return -1

	start = 0
	end = len(list) - 1

	while start + 1 < end:
		mid = int((start + end) / 2)

		if (list[mid] == target):
			start = mid
		elif (list[mid] < target):
			start = mid 
		else:
			end = mid 

	if list[end] == target:
		return end
	elif list[start] == target:
		return start

	return -1

def binarySearchRecur(list, target):
	if len(list) == 0:
		return -1

	list = sorted(list)

	return binarySearchHelper(list, 0, len(list)-1, target)

def binarySearchHelper(list, start, end, target):
	if start + 1> end:
		return -1
	mid = int((start + end) / 2)

	if list[mid] <= target:
		lastIndex = binarySearchHelper(list, mid+1, end, target)

		if lastIndex != -1:
			return lastIndex
		elif list[mid] == target:
			return mid
	else:
		return binarySearchHelper(list, start, mid-1, target)

	return -1

if __name__ == '__main__':
	list = [1, 2, 2, 2, 3]
	print(binarySearchRecur(list, 2))
	print(binarySearch(list, 2))