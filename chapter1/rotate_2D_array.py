'''
Created on Mar 17, 2016
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, 
write a method to rotate the image by 90 degrees. Can you do this in place?
@author: chunq
'''

def rotate2DArray(arrayToBeRotated, isCounterClockwise):
	totalLayers = len(arrayToBeRotated[0])
	for layer in range(0, int(totalLayers/2)):
		rotateOneLayer(arrayToBeRotated, layer, isCounterClockwise)
	return arrayToBeRotated

def rotateOneLayer(arrayToBeRotated, layer, isCounterClockwise):
	for position in range(layer, len(arrayToBeRotated[0]) - layer - 1):
		moveOneElement(arrayToBeRotated, layer, position, isCounterClockwise)
	return

def moveOneElement(arrayToBeRotated, start, position, isCounterClockwise):
	end = len(arrayToBeRotated[0]) - start - 1
	offset = position - start

	if isCounterClockwise:
		rotateOneElementClockwise(arrayToBeRotated, start, end, offset)
	else:
		rotateOneElementCounterClockwise(arrayToBeRotated, start, end, offset)
	return
	    
def rotateOneElementClockwise(arrayToBeRotated, start, end, offset):
	backUp = arrayToBeRotated[start][start + offset]
	arrayToBeRotated[start][start + offset] = arrayToBeRotated[end - offset][start]
	arrayToBeRotated[end - offset][start] = arrayToBeRotated[end][end - offset]
	arrayToBeRotated[end][end - offset] = arrayToBeRotated[start + offset][end]
	arrayToBeRotated[start + offset][end] = backUp

def rotateOneElementCounterClockwise(arrayToBeRotated, start, end, offset):
	backUp = arrayToBeRotated[start][start + offset]
	arrayToBeRotated[start][start + offset] = arrayToBeRotated[start + offset][end]
	arrayToBeRotated[start + offset][end] = arrayToBeRotated[end][end - offset]
	arrayToBeRotated[end][end - offset] = arrayToBeRotated[end - offset][start]
	arrayToBeRotated[end - offset][start] = backUp
	return

if __name__ == "__main__":
	print(rotate2DArray([[1,1,1],[2,2,2],[3,3,3]], False))
	print(rotate2DArray([[1,1,1],[2,2,2],[3,3,3]], True))
	print(rotate2DArray([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], True))
	print(rotate2DArray([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], False))