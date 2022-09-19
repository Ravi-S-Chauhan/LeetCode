class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        sign = 1;ans = 0;start = 0;
        if s[0] == '-':
            sign = 0
            start = 1
        elif s[0] == '+':
            sign = 1
            start = 1
        while start<len(s) and s[start].isdigit():
            ans = ans*10 + int(s[start])
            start +=1 
        ans = ans if sign else -ans
        if ans > 2147483647: return 2147483647
        elif ans < -2147483648: return -2147483648
        return ans
        