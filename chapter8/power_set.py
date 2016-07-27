'''
Power Set: Write a method to return all subsets of a set.
'''

import copy

def getPowerSet(set):
	if set is None:
		return None
	return getPowerSetHelper(set)

def getPowerSetHelper(set):
	if len(set) == 0:
		return [[]]
	subset = getPowerSetHelper(set[1:])
	moreSubset = copy.deepcopy(subset)
	for list in moreSubset:
		list.append(set[0])
	return subset + moreSubset

def getPowerSetTemplate(set):
	if set is None:
		return None
	getPowerSetTemplateHelper([], set, 0)
	return

def getPowerSetTemplateHelper(path, set, pos):
	print(path)

	for index in range(pos, len(set)):
		path.append(set[index])
		getPowerSetTemplateHelper(path, set, index+1)
		path.pop(len(path)-1)

	return

def getUniquePowerSet(set):
	if set is None:
		return None
	getUniquePowerSetHelper([], set, 0)
	return

def getUniquePowerSetHelper(path, set, pos):
	print(path)

	for index in range(pos, len(set)):
		if (index > 0) and (set[index -1] == set[index]):
			continue
		path.append(set[index])
		getUniquePowerSetHelper(path, set, index+1)
		path.pop(len(path)-1)

	return 


if __name__ == '__main__':
	set = [3,2]
	#my method
	print(getPowerSet(set))

	#template method
	print()
	getPowerSetTemplate(set)

	#unique power set template
	print()
	set = [1,1,2,2]
	getUniquePowerSet(set)


