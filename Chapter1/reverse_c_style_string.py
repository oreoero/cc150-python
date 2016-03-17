'''
Write code to reverse a C-Style String. (C-String means that 
abcd is represented as five characters, including the null character.)
@author: chwang
'''

def reverseCStyleString1(stringToReverse):
    newString = ""
    for char in reversed(stringToReverse):
        newString = newString + char
    return newString

def reverseCStyleString2(stringToReverse):
    newString = ""
    for char in stringToReverse[::-1]:
        newString = newString + char
    return newString

def reverseCStyleString3(stringToReverse):
    if len(stringToReverse) == 0:
        return ""
    newString = ""
    #the stop is omitted!
    for index in range(len(stringToReverse) - 1, -1, -1):
        newString = newString + stringToReverse[index]
    return newString

if __name__ == "__main__":
    testString = "Trick or treat"
    print(reverseCStyleString1(testString))
    print(reverseCStyleString2(testString))
    print(reverseCStyleString3(testString)) 

