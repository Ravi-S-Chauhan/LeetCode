class Solution {
public:
/*
    keep suming the elements and if the current sum is greater than max then update the max.
    if sum < 0 then we can freely remove them as they are only being a dead weight to the maximum sum

*/
    
    int maxSubArray(vector<int>& nums) {
        int sum = 0,mx = -INT_MAX;
        for(int i=0;i<nums.size();i++){
            sum+= nums[i];
            if (sum>mx)mx = sum;
            if (sum<0) sum = 0;
        }
        return mx;
    }
    
};