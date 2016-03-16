'''
Created on Mar 15, 2016
Implement an algorithm to determine if a string has all unique characters. 
What if you can not use additional data structures?
@author: chwang
'''

def hasUniqueChracters(stringToCheck):
    if len(stringToCheck) > 128:
        return 1
    letterAry = [None] * 128
    for letter in stringToCheck:
        if letterAry[ord(letter)-1]:
            return False
        else:
            letterAry[ord(letter)-1] = 1
    return True

if __name__ == "__main__":
    print(hasUniqueChracters("sstringToCheck"))
        
    
