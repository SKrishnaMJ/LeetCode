class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while(l<=r):
            mid = (l+r) // 2
            if target>nums[mid]:
                l=mid+1
            elif target<nums[mid]:
                r=mid-1
            else:
                if target==nums[l] and target==nums[r]:
                    return [l,r]
                if target!=nums[l]:
                    l+=1
                if target!=nums[r]:
                    r-=1
        return [-1,-1]
        