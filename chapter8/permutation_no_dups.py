'''
Permutations without Dups: Write a method to compute all permutations of a string
of unique characters.
'''

def getPerm(str):
	if str is None or len(str) == 0:
		return None
	return getPermHelper(str)

def getPermHelper(str):
	if len(str) == 0:
		return [""]
	firstChar = str[0]
	remainingPerm = getPermHelper(str[1:])
	results = []
	for str in remainingPerm:
		for index in range(0, len(str)+1):
			results.append(str[:index] + firstChar + str[index:])
	return results + remainingPerm

if __name__ == '__main__':
	print(getPerm("sb"))
	print(getPerm("sbc"))