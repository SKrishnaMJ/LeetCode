class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(k-1):
        #     nums.remove(max(nums))
        # return(max(nums))
        heapq.heapify(nums)
        l=heapq.nlargest(k,nums)
        return l[-1]
        