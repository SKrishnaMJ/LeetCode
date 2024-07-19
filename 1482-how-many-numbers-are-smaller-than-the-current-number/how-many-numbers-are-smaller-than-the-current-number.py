class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ctr=0
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[j]<nums[i]):
                    ctr+=1
            l.append(ctr)
            ctr=0
        return l

        