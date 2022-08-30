class Solution:
    """
1. Xor if same numbers is zeros i.e (1^1 = 0 => 1^1^4 => 4) using this property we find the xor of all the elements with their indexes which will result in zero.
2. We have an extra element which have occupied the place of missing element.
3. But that element would be N (size of nums) as one element is missing that we are finding. eg( in [0,1,3] 2 is missing element and 3 has occupied 3's place and the size of the list is 3)
4. return the solution of xor with ^ of N
    """
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0; N = len(nums); i =0;
        while i<N:
            xor = xor ^ i ^ nums[i]
            i += 1
        return xor ^ i