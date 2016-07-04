'''
Created on Mar 29, 2016
1.7 Write an algorithm such that if an element in an MxN matrix is 0, 
its entire row and column is set to 0.
@author: chunq
'''

def clearRowColumnInMatrix(matrix):
    rowHelper = [False] * len(matrix[0])
    columnHelper = [False] * len(matrix)
    
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if matrix[row][column] == 0:
                rowHelper[row] = True
                columnHelper[column] = True
                
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if rowHelper[row] or columnHelper[column]:
                matrix[row][column] = 0
    return matrix

if __name__ == "__main__":
    print(clearRowColumnInMatrix([[1,2,3],[1,0,3],[3,3,3]]))                