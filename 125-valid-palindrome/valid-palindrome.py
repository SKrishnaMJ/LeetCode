class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        f=0
        l=len(s)-1
        while(f<l):
            if s[f].isalnum() and s[l].isalnum() and s[f]!=s[l]:
                return False
            elif s[f].isalnum() and s[l].isalnum() and s[f]==s[l]:
                f+=1
                l-=1
            elif not s[f].isalnum():
                f+=1
            else:
                l-=1
        return True
        