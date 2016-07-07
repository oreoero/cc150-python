'''
Insertion: You are given two 32-bit number, N and M, and two bit positions, i and j. 
Write a method to insert M into N such that M starts at bit j and ends at bit i.
You can assume that the bits j through i have enough space to fit all of M. That is,
if M = 10011, you can assume that there are at least 5 bits between j and i.
'''

def bitInsert(M, N, i, j):
	'''
	exapmle: M = 1100, N =1111 0000, i = 5, j =2
	'''
	#1, clear j to i in N
	allOnes = ~0 #1111 1111

	left = allOnes << (i + 1) #1100 0000

	right = (1 << j) - 1 #0000 0100 - 0000 0001 = 0000 0011

	mask = left | right #1100 0011

	clearedN = mask ^ N #1100 0000

	#2, shift j bit M
	shiftedM = M << j #0011 0000

	#3, merge them and we're done
	return shiftedM | movedM #1111 0000

