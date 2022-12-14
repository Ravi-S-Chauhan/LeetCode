class Solution:
    """
    if we xor same numbers then the value is 0
    => if we xor all the value of the nums then we'll get the value which is only once.eg(1^1^2^3^3) => 2
    
    """
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans