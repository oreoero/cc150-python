'''
Created on Apr 10, 2016

There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check 
if they are one edit (or zero edit) away

@author: chunq
'''

def isOneAway(str1, str2):
    if len(str1) == len(str2):
        return isOneEditAway(str1, str2)
    elif len(str1) - len(str2) == 1:
        return isOneInsertAway(str1, str2)
    elif len(str2) - len(str1) == 1:
        return isOneInsertAway(str2, str1)
    return False

def isOneEditAway(str1, str2):
    hasDifference = False
    for index in range(0, len(str1)):
        if str1[index] != str2[index]:
            if hasDifference:
                return False
            else:
                hasDifference = True
    return True

def isOneInsertAway(longString, shortString):
    hasDifference = False
    index2 = 0
    for index in range(0, len(shortString)):
        index2 += 1
        if shortString[index] != longString[index2]:
            if hasDifference:
                return False
            else:
                hasDifference = True
                index2 += 1
    return True

if __name__ == '__main__':
    print(isOneAway('bale', 'pale'))
    print(isOneAway('apple', 'pple'))
    print(isOneAway('apple', 'pplde'))