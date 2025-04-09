class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l = 0
        while l<n-2:
            if nums[l]==0:
                ans+=1
                r=l
                while r<l+3 and r<n:
                    if nums[r]==0:
                        nums[r]=1
                    else:
                        nums[r]=0
                    r+=1
                l=l+1
            else:
                l+=1
        return ans if n==nums.count(1) else -1


        