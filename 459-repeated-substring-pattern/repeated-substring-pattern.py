class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        c=0
        n=len(s)
        for i in range(n-1):
            sub=s[:i+1]
            c=s.count(sub)
            if c*len(sub) == len(s):
                return True
        return False
        