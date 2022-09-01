class Solution:
    """
    3 pointer low,mid(initilaized to 0) and high(N-1) 
    run a while loop till mid<=high ->1,2,3
    1 if mid == 1 continue as we want 1 in the middle
    2 if mid == 0 swap with low and increment both as we want 1 in the begining
    3. if mid == 2 swap with high and decrement high not the mid
    as we have not yet came across high pointers element we dont want to miss 1 or 2
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = low = 0;high = len(nums)-1
        while mid<=high:
            if nums[mid] == 1 : 
                mid+= 1
            elif nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high-=1
                
        