class Solution {
public:
/*
    Keep Counting until ones until found zeros
    If found zeros and if CountZeros > maxCount => update value of maxCount
*/
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int CountOnes = 0,maxCount = 0;
        for (int i = 0;i<nums.size();i++){
            if (nums[i] == 1) CountOnes++;
            else {
                maxCount = max(CountOnes,maxCount);
                CountOnes = 0;
            }
        }
        maxCount = max(CountOnes,maxCount);
        return maxCount;
    }
};