class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = []
        mx = height[0]
        for i in range(len(height)):
            mx = max(mx,height[i])
            left.append(mx)
        mx = height[-1]
        for i in range(len(height)-1,-1,-1):
            mx = max(mx,height[i])
            right.append(mx)
        right = right[::-1]
        water = 0
        for i in range(len(height)):
            water += abs(min(left[i],right[i])-height[i])
        return water
        