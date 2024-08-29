class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans, ctr, neg = 0, 0, 0
        for i in range(len(costs)):
            if coins < costs[i]:
                neg+=1
                if (neg==len(costs)):
                    return 0
            if coins == ans:
                return ctr
            else:
                ans+=costs[i]
                if ans>coins:
                    return ctr
                ctr+=1
        return ctr
        