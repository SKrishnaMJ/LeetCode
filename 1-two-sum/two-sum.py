class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        l=len(nums)
        
        
        # for i in range(l-1):
        #     j=i+1
        #     if ((nums[i] + nums[j]) == target):
        #         return i,j
        #     else:
        #         j+=1
        for i in range(l-1):
            j=i+1
            for j in range (i+1, l):
                if ((nums[i] + nums[j]) == target):
                    return i, j
                    
