class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=''
        for i in range(len(word)):
            if word[i] != ch:
                res+=word[i]
            else:
                res=word[i]+res[::-1]
                res=res+word[i+1:]
                break
        return res
        