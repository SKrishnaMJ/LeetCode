class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in numSet:
            if i-1 not in numSet:
                l=1
                while i+l in numSet:
                    l+=1
                ans=max(l,ans)
        return ans
        