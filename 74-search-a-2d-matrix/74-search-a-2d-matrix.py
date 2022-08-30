class Solution:
    """
    starting from the top right corner if > target  move left else move below
    
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N,M = len(matrix),len(matrix[0])
        i,j = 0,M-1
        while i<N and j>-1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False