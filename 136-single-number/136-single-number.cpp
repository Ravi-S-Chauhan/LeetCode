class Solution {
public:
/*
    if we xor same numbers then the value is 0
    => if we xor all the value of the nums then we'll get the value which is only once.eg(1^1^2^3^3) => 2
*/
    int singleNumber(vector<int>& nums) {
        int xr = 0;
        for(auto i:nums){
            xr ^= i;
        }
        return xr;
    }
};