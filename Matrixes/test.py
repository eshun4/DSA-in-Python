def matrix(n):
    """ This function return an array of array conting number from the range of 0 to n."""
    return [[i for i in range(1, n)] for _ in range(n)]

def matrix_seq(n):
    """ This function return an array of array conting number from the range of 0 to n."""
    return [[i + j+ 1 for i in range(n)] for j in range(0, n*n, n)]

def matrix_middle(matrix):
    """ This function returns the middle element of a matrix."""
    row = len(matrix)
    column = len(matrix[0])
    row_middle = row // 2
    column_middle = column // 2
    return matrix[row_middle][column_middle]

def binarySearchMatrix(matrix, target):
    """ This function uses binary search for the target value in a MxM matrix."""
    row, col = 0, len(matrix[0]) - 1
    
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

def binarySearchMatrix2(matrix, target):
    """ This function uses binary search to find the target value in an MxM matrix.
    In the context of a 2D matrix, mid // cols and mid % cols are used to convert a 1D index to a 2D index.

    Here’s how it works:

    mid // cols: This operation performs integer division of mid by cols, which gives the row index. This is because in a row-major order 2D array (which is the default order in Python), you would traverse cols number of elements to move to the next row. So, mid // cols gives the number of such traversals you have made, i.e., the row index.
    mid % cols: This operation finds the remainder of mid divided by cols, which gives the column index. This is because after you’ve traversed some full rows (each of cols elements), you would be at some column in the next row. mid % cols gives the column index in that row.
    So, matrix[mid // cols][mid % cols] gives the element at the 2D index (row, col) in the matrix, where row is mid // cols and col is mid % cols.
    """
    row, col = len(matrix), len(matrix[0])
    left, right = 0, row * col - 1
    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // col][mid % col]
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
            
        
   

if __name__ == '__main__':
    print(matrix(4))
    print(matrix_seq(4))
    print('')
    matr = matrix_seq(4)
    print(matr)
    print(matrix_middle(matr))
    print('')
    print(binarySearchMatrix(matr, 12))
    print(binarySearchMatrix([[1,3]], 3))
    print('')
    print(binarySearchMatrix2(matr, 12))
    
    # matrix = [
    # [1, 3, 5, 7],
    # [10, 11, 16, 20],
    # [23, 30, 34, 50]]
    # target = 16
    # result = binarySearchMatrix(matrix, target)
    # print(f"Target {target} found: {result}")