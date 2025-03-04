class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans=[]
        i=0

        while(i<len(nums)):
            prev=nums[i]
            while i<len(nums)-1 and nums[i]+1 == nums[i+1]:
                i+=1
            if prev!=nums[i]:
                ans.append(str(prev)+'->'+str(nums[i]))
            else:
                ans.append(str(prev))
            i+=1
        return ans
