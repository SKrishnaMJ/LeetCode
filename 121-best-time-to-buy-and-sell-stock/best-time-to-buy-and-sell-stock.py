class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = float("inf")
        profit = 0
        for i in range(len(prices)):
            if prices[i]<price:
                price=prices[i]
            else:
                profit = max(profit, prices[i]-price)
        return profit
                
