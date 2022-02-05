class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        row = 0
        column = columns - 1
        
        while row >= 0 and column >= 0 and row < rows and column < columns:
            if matrix[row][column] > target:
                column = column - 1
            elif matrix[row][column] < target:
                row = row + 1
            else:
                return True
            
        return False