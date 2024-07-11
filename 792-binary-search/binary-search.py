class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = 0
        mid=0
        last = len(nums)-1
        if(len(nums)==1 and nums[0]==target):
            return 0
        while(first<=last):
            mid=(last-first//2)
            if(target == nums[mid]):
                return mid
            elif(target>nums[mid]):
                first=mid+1
            elif(target<nums[mid]):
                last=mid-1
        return -1
        