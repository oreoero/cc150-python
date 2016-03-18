'''
Created on Mar 17, 2016

Write a method to decide if two strings are anagrams or not.

@author: chunq
'''

def isAnagrams(firstString, secondString):
    sortedFirst = ''.join(sorted(firstString.lower().replace(" ", "")))
    sortedSecond = ''.join(sorted(secondString.lower().replace(" ", "")))
    return sortedFirst == sortedSecond

if __name__ == "__main__":
    print(isAnagrams(" ", "secondString"))
    print(isAnagrams("abb", "bba"))
    print(isAnagrams("Roll in the hay", "Thrill a honey"))