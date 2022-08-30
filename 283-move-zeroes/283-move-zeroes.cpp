class Solution {
public:
//     1. keep a count of zeros while traversing through the list.
//     2. If a non zeros element occurs then replace it with i-zerosCount position and give 0 to i th position.
    void moveZeroes(vector<int>& nums) {
        int zerosCount = 0,N = nums.size();
        for(int i= 0;i<N;i++){
            if (nums[i] == 0) zerosCount++;
            else if (zerosCount>0) {
                nums[i-zerosCount] = nums[i];
                nums[i] = 0;
            }
        }
        
    }
};