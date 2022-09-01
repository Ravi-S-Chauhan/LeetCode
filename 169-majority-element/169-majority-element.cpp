class Solution {
public:
/*
    If count == 0 initialize the ele with current element and count increment to 1 else if curr is same as the ele variable increase the count else if curr is not same as the ele variable decrement count. This works because there always exists the element whose frequency is > n/2
*/
    int majorityElement(vector<int>& nums) {
        int count=0,ele;
        for(int i = 0;i<nums.size();i++){
            if (count == 0){
                ele = nums[i];
                count++;
            }
            else if (ele == nums[i]) count++;
            else count--;
        }
        return ele;
    }
};