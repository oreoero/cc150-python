'''
Design an algorithm and write code to remove the duplicate characters 
in a string without using any additional buffer. NOTE: One or two additional 
variables are fine. An extra copy of the array is not.

FOLLOW UP
Write the test cases for this method.
Created on Mar 16, 2016

@author: chunq
'''

def removeDuplicateCharsWithArray(stringToRemove):
    charAry = [None] * 128
    newString = ""
    for char in stringToRemove:
        if charAry[ord(char)]:
            continue
        else:
            newString = newString + char
            charAry[ord(char)] = True
    return newString
            
def removeDuplicateCharsWithoutArray(stringToRemove):
    newString = ""
    for index1 in range(0, len(stringToRemove)):
        foundDuplicate = False
        for index2 in range(index1 + 1, len(stringToRemove)):
            if stringToRemove[index1] == stringToRemove[index2]:
                foundDuplicate = True
                break
        if foundDuplicate:
            continue
        else:
            newString = newString + stringToRemove[index1]
    return newString
    
if __name__ == "__main__":
    print(removeDuplicateCharsWithArray("sstringToCheck"))
    print(removeDuplicateCharsWithArray("aaaa"))
    print(removeDuplicateCharsWithArray("abba"))
    print(removeDuplicateCharsWithArray(""))
    print(removeDuplicateCharsWithoutArray("sstringToCheck"))
    print(removeDuplicateCharsWithoutArray("aaaa"))
    print(removeDuplicateCharsWithoutArray("aabb"))
    print(removeDuplicateCharsWithoutArray(""))
        
    
    