class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        1. keep a count of zeros while traversing through the list.
        2. If a non zeros element occurs then replace it with i-zerosCount position and give 0 to i th position.
        """
        zeros = 0
        N = len(nums)
        for i in range(N):
            if nums[i] == 0:
                zeros+= 1
            elif zeros>0:
                nums[i],nums[i-zeros] = nums[i-zeros],nums[i]
        
        