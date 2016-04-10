'''
Created on Apr 10, 2016

Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to 
be limited to just dictionary words.

@author: chunq
'''

def isPalindromePermutation(stringToCheck):
    stringToCheck = stringToCheck.lower()
    stringToCheck = stringToCheck.replace(' ','')
    
    charAry = [0] * 256
    for char in stringToCheck:
        charAry[ord(char)] += 1
    
    hasMultiSingleChar = False
    
    for index in range(0, 256):
        if charAry[index] % 2 != 0:
            if hasMultiSingleChar:
                return False
            else:
                hasMultiSingleChar = True
    
    return True

if __name__ == '__main__':
    print(isPalindromePermutation('Tact coa'))
    print(isPalindromePermutation('Tact coa'))
        
