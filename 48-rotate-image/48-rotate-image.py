class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        1. Transpose of the matrix
        2. Reverse each row i.e list
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        
        