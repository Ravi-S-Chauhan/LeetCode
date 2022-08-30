class Solution {
public:
/*  0. Keep sum of A[i].
    1. Check if we have a sum-k in map  ...=> sum+A[i] == k => A[i] == sum-k
    2. if yes then increment the count with number of sum-k we have
    3. Add the sum to map.
*/
    int subarraySum(vector<int>& nums, int k) {
        map<int,int> mp;
        mp.insert(pair<int,int>(0,1));
        int sum = 0,count = 0;
        for(int i = 0;i<nums.size();i++){
            sum += nums[i];
            if(mp.find(sum-k)->second)count += mp.find(sum-k)->second;
            mp[sum] = mp[sum]+1;
        }
        return count;
    }
};