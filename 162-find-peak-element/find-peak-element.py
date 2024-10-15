class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans=0
        low=0
        high=len(nums)-1
        mid=0
        while(low<high):
            mid=int(low+high)//2
            if nums[mid] < nums[mid+1]:
                low=mid+1
            else:
                high=mid
        return low
        