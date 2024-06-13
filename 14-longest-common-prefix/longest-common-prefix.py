class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        l =len(prefix)
        for i in strs[1:]:
            while(prefix != i[:l]):
                l = l-1
                if(l==0):
                    return ""
                else:
                    prefix = prefix[:l]
        return prefix
        