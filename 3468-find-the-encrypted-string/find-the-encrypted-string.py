class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        str=''
        if (len(s) == 1):
            return s
        while(k >= len(s)):
            k=k-len(s)
        for ch in range(len(s)):
            str=str+s[k]
            k=k+1
            if(k==len(s)):
                k=0
        return str

        