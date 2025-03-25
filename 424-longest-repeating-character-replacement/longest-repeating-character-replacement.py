class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = [0]*26
        i = 0
        longest = 0
        for j in range(len(s)):
            c[ord(s[j])-65]+=1
            while ((j-i)+1) - max(c) > k:
                c[ord(s[i])-65]-=1
                i+=1
            longest = max(longest, (j-i)+1)
        return longest


