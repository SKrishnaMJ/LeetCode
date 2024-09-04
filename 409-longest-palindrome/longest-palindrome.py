class Solution:
    def longestPalindrome(self, s: str) -> int:
        res_set=set()
        res=0
        for ch in s:
            if ch in res_set:
                res_set.remove(ch)
                res+=2
            else:
                res_set.add(ch)
        if res_set:
            res+=1
        return res
            
