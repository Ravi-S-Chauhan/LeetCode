class Solution {
public:
/*
    3 pointer low,mid(initilaized to 0) and high(N-1) 
    run a while loop till mid<=high ->1,2,3
    1 if mid == 1 continue as we want 1 in the middle
    2 if mid == 0 swap with low and increment both as we want 1     in the begining
    3. if mid == 2 swap with high and decrement high not the        mid
    as we have not yet came across high pointers element we         dont want to miss 1 or 2
*/
    void swap(vector<int>& nums,int i,int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
    void sortColors(vector<int>& nums) {
        int N = nums.size();
        int low=0,mid=0,high=N-1;
        while(mid<=high){
            if (nums[mid] == 1)mid++;
            else if (nums[mid] == 0){
                swap(nums,low,mid);
                low++;mid++;
            }
            else{
                swap(nums,high,mid);
                high--;
            }
        }
    }
};




