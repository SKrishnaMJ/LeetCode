class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy=prices[0]
        price=0
        for sell in range(1, len(prices)):
            if(buy>prices[sell]):
                buy = prices[sell]
            price = max(price, prices[sell]-buy)
        return price
        