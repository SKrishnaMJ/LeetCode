class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ctr=0
        for i in jewels:
            for j in stones:
                if i==j:
                    ctr+=1
        return ctr
        