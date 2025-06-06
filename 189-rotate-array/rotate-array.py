class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        n=len(nums)
        def reverse(i,j):
            while i<j:
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k, len(nums)-1)
        