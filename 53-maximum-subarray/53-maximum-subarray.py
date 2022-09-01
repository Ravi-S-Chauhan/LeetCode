class Solution:
    """
    keep suming the elements and if the current sum is greater than max then update the max.
    if sum < 0 then we can freely remove them as they are only being a dead weight to the maximum sum
    """
    def maxSubArray(self, nums: List[int]) -> int:
        sm = 0;mx = -sys.maxsize
        for i in nums:
            sm += i
            mx = max(mx,sm)
            if sm<0 : sm = 0
        return mx