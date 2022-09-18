class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(pow(2,len(nums))):
            temp = []
            for j in range(len(nums)):
                if i & 1<<j:
                    temp.append(nums[j])
            result.append(temp)
        result.sort()
        return result