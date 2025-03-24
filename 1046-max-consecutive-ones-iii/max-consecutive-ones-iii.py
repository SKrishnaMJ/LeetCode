class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        c = 0
        i=0
        for j in range(len(nums)):
            if nums[j]==0:
                c+=1
            while c>k:
                if nums[i]==0:
                    c-=1
                i+=1
            longest = max(longest, (j-i)+1)
        return longest



        