class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        setx = set()
        i=0
        maxlen=0
        for j in range(l):
            while s[j] in setx:
                setx.remove(s[i])
                i+=1
            setx.add(s[j])
            maxlen = max(maxlen, j-i+1)

                    
        return maxlen




        