class Solution {
public:
/*
    keep suming the elements and if the current sum is greater than max then update the max.
    if sum < 0 then we can freely remove them as they are only being a dead weight to the maximum sum

*/
    
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0],mx = nums[0];
        for(int i=1;i<nums.size();i++){
            if (sum<0) sum = 0;
            sum+= nums[i];
            if (sum>mx)mx = sum;
        }
        return mx;
    }
    
};