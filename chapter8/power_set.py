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

if __name__ == '__main__':
	set = [3,2]
	print(getPowerSet(set))
