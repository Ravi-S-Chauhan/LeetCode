class Solution {
public:
/*
    starting from the top right corner if > target  move left else move below
*/
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int N=matrix.size(),M=matrix[0].size();
        int i=0,j=M-1;
        while (j>-1 & i<N){
            if ( matrix[i][j] == target ) return true;
            else if (matrix[i][j]>target) j--;
            else i++;
        }
        return false;
    }
};