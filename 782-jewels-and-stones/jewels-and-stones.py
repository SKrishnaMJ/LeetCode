class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = dict(Counter(stones))
        ans=0
        for j in jewels:
            if j in c:
                ans+=c[j]
        return ans
        