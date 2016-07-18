'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows
and c colomns. The robot can only move in two directions, right an down, but certain
cells are "off limits" such that the robot cannot step on them. Design an algorithm
to find a path for the robot from the top left to the bottom right.
'''

def findPath(block):
	path = []
	if findPathHelper(block, len(block)-1, len(block[0])-1, path):
		return path
	else:
		return None

def findPathHelper(block, row, column, path):
	if row < 0 or column < 0 or block[row][column]:
		return False

	if row == 0 and column == 0:
		isStart = True
	else:
		isStart = False

	if isStart or findPathHelper(block, row-1, column, path) or findPathHelper(block, row, column-1, path):
		path.append([row, column])
		return True
	else:
		return False

if __name__ == '__main__':
	block = [[False, False, False], [False, True, True], [False, False, False]]
	print(findPath(block))
	block = [[False, False, False], [True, True, True], [False, False, False]]
	print(findPath(block))