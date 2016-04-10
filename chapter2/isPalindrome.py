'''
Created on Apr 10, 2016

Implement a function to check if a linked list is a palindrome

@author: chunq
'''
from math import ceil

def isPalindrome(listToCheck):
    for index in range(0, ceil(len(listToCheck)/2)):
        if listToCheck[index] != listToCheck[len(listToCheck) - 1 - index]:
            return False
    return True

if __name__ == '__main__':
    print(isPalindrome([0]))
    print(isPalindrome([0,0]))
    print(isPalindrome([0,0,0]))
    print(isPalindrome([0,0,1]))