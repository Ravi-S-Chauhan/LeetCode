class Solution {
public:
    bool check(vector<int>& nums) {
        int k = 0;int N = nums.size();
        for(int i = 0;i<N;i++){
            if (nums[i]>nums[(i+1)%N]) k++;
            if (k>1){
                return false;
            }
        }
        return true;
    }
};