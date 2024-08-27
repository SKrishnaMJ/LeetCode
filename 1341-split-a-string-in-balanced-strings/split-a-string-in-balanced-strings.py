class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal=0
        ctr=0
        for char in s:
            if char == 'R':
                ctr+=1
            else:
                ctr-=1
            if ctr==0:
                bal+=1
        return bal
        