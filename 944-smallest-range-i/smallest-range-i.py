class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        l=min(nums)+k
        r=max(max(nums)-k, l)
        return r-l
        
        