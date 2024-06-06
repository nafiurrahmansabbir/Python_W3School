import numpy as np

def multiply_diagonals(matrix1, matrix2):
    # Ensure the input arrays are numpy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)
    
    # Get the diagonals of the matrices
    diag1 = np.diagonal(matrix1)
    diag2 = np.diagonal(matrix2)
    print(diag1)
    print(diag2)
    
    # Multiply the diagonals element-wise
    multiplied_diagonals = diag1 * diag2
    
    return multiplied_diagonals

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = multiply_diagonals(matrix1, matrix2)
print("Multiplied Diagonal Elements: ", result)
