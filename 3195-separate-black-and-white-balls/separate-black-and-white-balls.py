class Solution:
    def minimumSteps(self, s: str) -> int:
        ans,black=0,0
        for ch in s:
            if ch == "0":
                ans+=black
            else:
                black+=1
        return ans