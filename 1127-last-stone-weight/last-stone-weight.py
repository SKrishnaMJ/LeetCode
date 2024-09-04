class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort(reverse=True)
            l=max(stones)
            stones.remove(l)
            r=max(stones)
            stones.remove(r)
            if l!=r:
                stones.append(l-r)
        return stones[0] if len(stones)>0 else 0
        
        