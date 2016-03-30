'''
Created on Mar 29, 2016
1.8 Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one 
@author: chunq
'''

def isRotateString(a,b):
    if len(a) != len(b):
        return False
    return b in (a + a)

if __name__ == "__main__":
    print(isRotateString("","Hello"))
    print(isRotateString("erbottlewat","waterbottle"))
    print(isRotateString("","Hello"))