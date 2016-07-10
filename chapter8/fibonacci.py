'''
Write a method to generate the nth Fibonacci number.
'''

def fibonacci(n):
	if n <= 0:
		return 0
	if n == 1:
		return 1
	return n + fibonacci(n-1)

if __name__ == '__main__':
	print(fibonacci(4))
	print(fibonacci(14))
	print(fibonacci(0))