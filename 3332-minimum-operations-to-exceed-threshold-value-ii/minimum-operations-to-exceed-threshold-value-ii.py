class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res=0
        heapq.heapify(nums)
        while any(num<k for num in nums):
            
            f=heapq.heappop(nums)
            s=heapq.heappop(nums)
            heapq.heappush(nums, min(f, s) * 2 + max(f, s))
            res+=1
        return res

        