'''
Magic Index: A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i. 
Given a sorted array of distinct integers, write a method to find a magic index, if one exists,
in array A.

Follow Up: What if the values are not distinct?
'''

def getMagicIndex(sortedArray):
	return getMagicIndexHelper(sortedArray, 0, len(sortedArray)-1)

def getMagicIndexHelper(sortedArray, start, end):
	if start > end:
		return
	mid = int((start + end) / 2)
	if mid == sortedArray[mid]:
		return mid
	elif mid < sortedArray[mid]:
		return getMagicIndexHelper(sortedArray, 0, mid-1)
	else:
		return getMagicIndexHelper(sortedArray, mid+1, end)

if __name__ == '__main__':
	test = [x**2 - 1 for x in range(1,4)]
	print(getMagicIndex(test))