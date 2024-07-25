class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=[]
        while(0 in nums):

            a=nums.remove(0)
            l.append(a)
        for i in range(len(l)):
            nums.append(0)


        
        