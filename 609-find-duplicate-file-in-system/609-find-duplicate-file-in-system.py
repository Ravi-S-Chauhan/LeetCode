class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def contents(s):
            tmep = s.split('(')
            return tmep[-1][:-1]
        def fName(s):
            temp = s.split('(')
            return temp[0]
        def solve(s):
            h = [i for i in s.split(' ')]
            for i in range(1,len(h)):
                mp[contents(h[i])].append(h[0]+"/"+fName(h[i]))
        mp = defaultdict(list)
        for i in paths:
            solve(i)
        print(mp)
        return [v for k,v in mp.items() if len(v)>1]