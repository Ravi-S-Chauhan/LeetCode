class Solution:
    """
    If count == 0 initialize the ele with current element and count increment to 1 else if curr is same as the ele variable increase the count else if curr is not same as the ele variable decrement count. This works because there always exists the element whose frequency is > n/2
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = 0;ele = -1
        for curr in nums:
            if count == 0:
                count+= 1
                ele = curr
            elif ele == curr:
                count+= 1
            else: count-= 1
        return ele
    
    
    