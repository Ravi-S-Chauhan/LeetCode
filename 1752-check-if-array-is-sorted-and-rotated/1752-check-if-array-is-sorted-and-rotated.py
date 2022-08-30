class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums);k =0
        for i in range(N):
            if nums[i]>nums[(i+1)%N]:
                k += 1
                if k> 1:
                    return False
        return True