'''
Write a function that accepts a square matrix ( 2D array) and returns the determinant of the matrix.N x N

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

A 1x1 matrix has determinant .|a|a

A 2x2 matrix or[ [a, b], [c, d] ]

|a  b|
|c  d|
has determinant: .a*d - b*c

The determinant of an sized matrix is calculated by reducing the problem to the calculation of the determinants of matrices of size.n x nnn-1 x n-1

For the 3x3 case, or[ [a, b, c], [d, e, f], [g, h, i] ]

|a b c|  
|d e f|  
|g h i|  
the determinant is: where refers to taking the determinant of the 2x2 matrix created by crossing out 
the row and column in which the element a occurs:a * det(a_minor) - b * det(b_minor) + c * det(c_minor)det(a_minor)

|- - -|
|- e f|
|- h i|  
Note the alternation of signs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row , then:[a, b, c, d]

det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
'''





def minor_matrix(matrix, index):
    intermediate_matrix=[]
    new_matrix=[]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if  i!=0 and j!=index:
                intermediate_matrix.append(matrix[i][j])
        if len(intermediate_matrix) == 0:
            pass
        else:
            new_matrix.append(intermediate_matrix)
            intermediate_matrix = []
    return(new_matrix);
   
                    
def determinant(matrix):
    sum_elements = 0
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1];
    else:
        for i in range(len(matrix)):
            if matrix[0][i] == 0:
                pass
            elif i % 2 == 0:
                sum_elements += matrix[0][i] * determinant(minor_matrix(matrix, i))
            else:
                sum_elements -= matrix[0][i] * determinant(minor_matrix(matrix, i))
    return  sum_elements;

