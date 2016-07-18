def playTowerOfHanoi(N):
	playTowerOfHanoiHelper(N, 1, 3)

def playTowerOfHanoiHelper(N, source, destination):
	if N == 1:
		print("Move " + str(N) + " from " + str(source) + " to " + str(destination))
	else:
		buffer = 6 - source - destination                                                                            
		playTowerOfHanoiHelper(N-1, source, buffer)
		print("Move " + str(N) + " from " + str(source) + " to " + str(destination))
		playTowerOfHanoiHelper(N-1, buffer, destination)

if __name__ == '__main__':
	playTowerOfHanoi(3)