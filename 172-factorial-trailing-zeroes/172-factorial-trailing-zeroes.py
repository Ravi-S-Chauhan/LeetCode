class Solution:
    def trailingZeroes(self, n: int) -> int:
        i = 5; count = 0
        while i<=n:
            count += floor(n/i)
            i *= 5
        return count