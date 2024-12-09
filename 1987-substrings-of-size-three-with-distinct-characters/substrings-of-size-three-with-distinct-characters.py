class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        words=[]
        i=0
        res=0
        while i+3<=len(s):
            words.append(s[i:i+3])
            i+=1

        for word in words:
            if word.count(word[0])>1 or word.count(word[1])>1 or word.count(word[2])>1:
                continue
            else:
                res+=1
        return res
        