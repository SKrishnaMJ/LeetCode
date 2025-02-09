class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        prev=nums[0]
        for j in range(1,len(nums)):
            if (prev%2==0 and nums[j]%2==0) or (prev%2!=0 and nums[j]%2!=0):
                return False
            else:
                prev=nums[j]
                    
        return True
        