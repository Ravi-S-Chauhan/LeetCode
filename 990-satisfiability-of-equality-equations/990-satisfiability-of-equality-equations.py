class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if t[x] != x:
                (t[x]) = find(t[x])
            return t[x]
        t = {a:a for a in ascii_lowercase}
        for a,e,_,b in equations:
            if e == '=':
                t[find(a)] = find(b)
        return not any(e == '!' and find(a) == find(b) for a,e,_,b in equations)