class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = sorted(list(zip(efficiency,speed)),reverse = True)
        res = 0;speed = 0;minHeap = []
        for eff,spd in eng:
            if len(minHeap) == k:
                speed -= heappop(minHeap)
            speed += spd
            heappush(minHeap,spd)
            res = max(res,speed*eff)
        return res%(10**9+7)
