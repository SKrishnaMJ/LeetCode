class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:

            if s.count(ch) < t.count(ch)>1:
                return ch
            elif ch not in s:
                return ch

            # if ((ch not in s) or (t.count(ch)==2 and s.count(ch)==1)):
            #     return ch
           
        