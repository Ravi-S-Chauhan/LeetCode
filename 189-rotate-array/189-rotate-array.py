
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        
        1. Reverse the array completely
        2. Reverse the array from 0 to k-1 and k to N-1
        
        """
        def rev(nums,i,j):
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        N = len(nums)
        if k>N:
            k = k%N
        if N == 1:
            return
        rev(nums,0,N-1)
        rev(nums,0,k-1)
        rev(nums,k,N-1)
        
            
            
        