class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        for s in strs:
            min_len = min(min_len, len(s))
        i = 0
        while i<min_len:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
            # Below return is for edge cases in case strs=[" "] or strs=["a"]
        return s[:i]

        
        