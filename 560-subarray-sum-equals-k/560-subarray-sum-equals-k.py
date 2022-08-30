class Solution:
    """
    0. Keep sum of A[i].
    1. Check if we have a sum-k in map  ...=> sum+A[i] == k => A[i] == sum-k
    2. if yes then increment the count with number of sum-k we have
    3. Add the sum to map.
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        mx = sm = 0
        d = {0:1}
        for i in range(len(nums)):
            sm += nums[i]
            if sm-k in d:
                mx += d[sm-k]
            d[sm] = d.get(sm,0)+1
        return mx