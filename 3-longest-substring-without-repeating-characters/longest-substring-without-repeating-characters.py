class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        setx = set()
        win = 0
        for r in range(len(s)):
            while s[r] in setx:
                setx.remove(s[l])
                l+=1
            setx.add(s[r])
            win = (r-l)+1
            longest = max(longest,win)
        return longest






        