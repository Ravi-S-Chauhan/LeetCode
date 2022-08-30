class Solution:
    """
    1. We will search for nums[i]-target in map. If found we can directly return it that elements index and current index
    2. If not found then we can add that number to the map for future use
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            if target-nums[i] in mp:
                return [i,mp[target-nums[i]]]
            mp[nums[i]] = i
        return -1