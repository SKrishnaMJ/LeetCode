class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum())
        s= s.lower()
        l = len(s)-1
        f=0
        while(f<l):
            if(s[f]==s[l]):
                f+=1
                l-=1
            else:
                return False
        return True