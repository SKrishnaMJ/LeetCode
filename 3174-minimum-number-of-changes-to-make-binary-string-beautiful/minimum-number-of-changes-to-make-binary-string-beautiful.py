class Solution:
    def minChanges(self, s: str) -> int:
        l=list(s)
        ctr=0
        for i in range(0, len(l)-1,2):
            if l[i] != l[i+1]:
                ctr+=1
        return ctr
        
        