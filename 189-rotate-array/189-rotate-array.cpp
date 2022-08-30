class Solution {
public:
    
//     1. Reverse the array completely
//     2. Reverse the array from 0 to k-1 and k to N-1
    
    void rev(vector<int>& nums,int i,int j){
        while (i<j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;j--;
        }
    }
    void rotate(vector<int>& nums, int k) {
        int N = nums.size();
        if (N == 1) return;
        if (k>N) k = k%N;
        rev(nums,0,N-1);
        rev(nums,0,k-1);
        rev(nums,k,N-1);
        
    }
};