class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def contents(s):
            tmep = s.split('(')
            return [tmep[0],tmep[-1][:-1]]
        def solve(s):
            h = [i for i in s.split(' ')]
            for i in range(1,len(h)):
                a,b = contents(h[i])
                mp[b].append(h[0]+"/"+a)
        mp = defaultdict(list)
        for i in paths:
            solve(i)
        print(mp)
        return [v for k,v in mp.items() if len(v)>1]