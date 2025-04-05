class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        heap = []
        for st in stones:
            heap.append(-st)
            heapq.heapify(heap)
        while heap and len(heap)>1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -1*(x-y))
            
        return -heap[0] if len(heap)==1 else 0

        