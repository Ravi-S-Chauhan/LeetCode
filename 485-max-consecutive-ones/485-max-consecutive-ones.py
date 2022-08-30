class Solution:
    """
    1. Keep Counting until ones until found zeros
    2. If found zeros and if CountZeros > maxCount => update value of maxCount
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0;N = len(nums)
        mx = 0
        for i in range(N):
            if nums[i] == 1:
                count += 1
            elif nums[i]== 0:
                mx = max(mx,count)
                count = 0
        mx = max(mx,count)
        return mx