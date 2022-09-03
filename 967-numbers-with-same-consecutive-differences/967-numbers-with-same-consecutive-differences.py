class Solution:
    """
    Explanation
    We initial the current result with all 1-digit numbers,
    like cur = [1, 2, 3, 4, 5, 6, 7, 8, 9].

    Each turn, for each x in cur,
    we get its last digit y = x % 10.
    If y + K < 10, we add x * 10 + y + K to the new list.
    If y - K >= 0, we add x * 10 + y - K to the new list.

    We repeat this step N - 1 times and return the final result.


    Complexity
    If K >= 5, time and Space O(N)
    If K <= 4, time and space O(2^N)
    """
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = [1,2,3,4,5,6,7,8,9]
        for i in range(1,n):
            temp = []
            for x in cur:
                y = x%10
                if y+k<10 : temp.append(x*10+y+k)
                if k and y-k>=0 : temp.append(x*10+y-k)
            cur = temp
        return cur