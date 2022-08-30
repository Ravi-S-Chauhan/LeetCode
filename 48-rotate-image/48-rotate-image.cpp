class Solution {
public:
/*
1. Transpose of the matrix
2. Reverse each row i.e vector<int> 
*/
    void rotate(vector<vector<int>>& matrix) {
        for (int i = 0;i<matrix.size();i++){
            for(int j = 0;j<i;j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0;i<matrix.size();i++){
            reverse(matrix[i].begin(),matrix[i].end());
        }
    }
};