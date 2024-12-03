class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j,c=0,0
        ans=""
        for i in range(len(s)):
            if i==spaces[j]:
                ans+=s[c:spaces[j]]+" "
                j+=1
                c=i
                if (j==len(spaces)):
                    break
        ans+=s[c:]
        return ans
        