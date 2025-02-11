class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res=''
        i=0
        while(i<len(s)):
            if part==s[i:len(part)+i]:
                s=res+s[len(part)+i:]
                i=0
                res=''
            else:
                res+=s[i]
                i+=1
        return res