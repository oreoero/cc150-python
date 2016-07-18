'''
Permutations with Duplicates: Write a method to compute all permutations of a 
string whose character are not necessarily unique. The list of permutations
should not have duplicates
'''

def getPerm(str):
	strInDict = {}

	for char in str:
		if char in strInDict:
			strInDict[char] += 1
		else:
			strInDict[char] = 1

	return getPermHelper(strInDict)

def getPermHelper(strInDict):
	result = []
	#loop through each key
	for key in strInDict.keys():
		if strInDict[key] > 0:
			#reduce one char
			strInDict[key] = strInDict[key] - 1
			resultTemp = getPermHelper(strInDict)
			#add the char back
			strInDict[key] = strInDict[key] + 1

			#append first char to other results
			for str in resultTemp:
				result.append(key + str)
	#base case
	if len(result) == 0: result.append('')
	return result

if __name__ == '__main__':
	print(getPerm('aa'))
	print(getPerm('aab'))
	print(getPerm('aabc'))