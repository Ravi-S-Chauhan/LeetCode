class Solution {
public:
/*
    1. We will search for nums[i]-target in map. If found we can directly return it that elements index and current index
    2. If not found then we can add that number to the map for future use
*/
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> mp;
        vector<int> result;
        for(int i=0;i<nums.size();i++){
            if (mp.find(target-nums[i])!=mp.end()){
                result.push_back(mp[target-nums[i]]);
                result.push_back(i);
                return result;
            }
            mp[nums[i]] = i;
        }
        return result;
        
    }
};