class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count = 0,N = nums.size();
        for (int i =1;i<N;i++){
            if (nums[i] == nums[i-1]) count++;
            else nums[i-count] = nums[i];
        }
        return N-count;
    }
};