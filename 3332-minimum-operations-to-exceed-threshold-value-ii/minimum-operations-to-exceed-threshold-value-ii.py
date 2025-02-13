class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        min_heap=nums
        heapq.heapify(nums)
        while min_heap[0]<k:
            
            f=heapq.heappop(nums)
            s=heapq.heappop(nums)
            heapq.heappush(nums, min(f, s) * 2 + max(f, s))
            res+=1
        return res

        