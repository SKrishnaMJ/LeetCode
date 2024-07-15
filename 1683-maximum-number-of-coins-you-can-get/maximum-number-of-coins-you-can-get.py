class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans=0
        for i in range(len(piles)//3):
            piles.pop()
            ans=ans+piles.pop()
            piles.pop(0)
        return ans
        