def checkIfMatrixIsValid(matrix):
    #length = len(matrix[0])
    #print matrix.isArray
    if type(matrix[0]) is not list:
        return False
    if (len(matrix) == 1):
        return True
    length = len(matrix[0])
   
    for i in range(1,len(matrix)):
        #print len(matrix[i])
        if (length != len(matrix[i])):
            return False
    return True

def getMatrixSize(matrix):
    if(checkIfMatrixIsValid(matrix)):
        return [len(matrix),len(matrix[0])]
    else:
        return []

def getRow(matrix, rowIndex):
    if(checkIfMatrixIsValid(matrix)):
        size = getMatrixSize(matrix)
        if(rowIndex > size[0]):
            return []
        else:
            return matrix[rowIndex]
    else:
        return []

def getColumn(matrix, columnIndex):
    if(checkIfMatrixIsValid(matrix)):
        size = getMatrixSize(matrix)
        if(columnIndex > size[1]):
            return []
        else:
            column = []
            #print size[1]
            for i in range(0,size[0]):
                column.append(matrix[i][columnIndex])
            return column
    else:
        return []

def transposeMatrix(matrix):
    if(checkIfMatrixIsValid(matrix)):
        transpose = []
        for i in range(0,(getMatrixSize(matrix))[1]):
            transpose.append(getColumn(matrix,i))
        return transpose
    else:
        return None

def dotProduct(row,column):
    if(len(row) != len(column)):
        return None
    else:
        product = [0] * len(row)
        for i in range(0,len(row)):
            product[i] = row[i] * column[i]
        return sum(product)

def multiplyMatrices(matrix1,matrix2):
    print getMatrixSize(matrix1)
    print getMatrixSize(matrix2)
    if(checkIfMatrixIsValid(matrix1) and checkIfMatrixIsValid(matrix2)):
        if(((getMatrixSize(matrix1)[0] == getMatrixSize(matrix2)[1])) and (getMatrixSize(matrix1)[1] == getMatrixSize(matrix2)[0])):
            if(getMatrixSize(matrix1)[1] == getMatrixSize(matrix2)[0]):
                multmatrix = [[0] * getMatrixSize(matrix2)[1] for i in range(getMatrixSize(matrix1)[0])]
                for i in range(getMatrixSize(matrix1)[0]):
                    for j in range(getMatrixSize(matrix1)[0]):
                        multmatrix[i][j] = dotProduct(getRow(matrix1,i),getColumn(matrix2,j))
                return multmatrix
            else:
                return None
        else:
            return None
    else:
        return None

def main():
    print checkIfMatrixIsValid([1,2,3])
    print getMatrixSize([[2,3,4],[2,3,4],[3,4]])
    print getRow([[1,2,3],[1,2,3],[3,4]],1)
    print getColumn([[1,2,3],[3,4,2]],1)
    print transposeMatrix(([[1,2,3],[3,4,2]]))
    print dotProduct([6,2,9,0],[1,3,2,1])    
    print multiplyMatrices([[9,10],[6,3],[10,4]],[[7,0,4],[5,4,1]])
    
    
if __name__ == "__main__":
    main()