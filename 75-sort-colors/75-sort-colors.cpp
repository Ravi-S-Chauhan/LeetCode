class Solution {
public:
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