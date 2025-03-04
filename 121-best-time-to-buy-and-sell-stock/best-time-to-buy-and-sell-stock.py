class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        price = float("inf")
        for i in range(len(prices)):
            if prices[i]<price:
                price=prices[i]
            else:
                profit=max(profit, prices[i]-price)
        return profit
                
