class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s=bin(start)
        s=s[2:]
        g=bin(goal)
        g=g[2:]
        c=0
        if len(s)>len(g):
            n = len(s)-len(g)
            g='0'*n + g
        elif len(g)>len(s):
            n = len(g) - len(s)
            s = '0' * n + s
        for i in range(len(s)-1,-1,-1):
            if s[i]!=g[i]:
                c+=1
        return c

        