class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        while goal>0 or start>0:
            if start%2 != goal%2:
                ans += 1
            start >>= 1
            goal >>= 1
            # print(start,goal,ans)
        return ans
        