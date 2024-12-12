class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-g for g in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            n=-heapq.heappop(gifts)
            n**=0.5
            heapq.heappush(gifts,int(-n))
        return -sum(gifts)