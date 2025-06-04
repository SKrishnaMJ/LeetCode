class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        l = 0
        r = len(s)-1
        while l<r:
            if t[l].isalnum() and t[r].isalnum() and t[l]!=t[r]:
                return False
            elif not t[l].isalnum():
                l+=1
            elif not t[r].isalnum():
                r-=1
            else:
                l+=1
                r-=1
        return True
        