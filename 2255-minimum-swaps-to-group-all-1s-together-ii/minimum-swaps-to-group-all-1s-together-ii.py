class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        arr = nums + nums
        ans = float('inf')
        l = 0
        r = total_ones - 1
        sm = sum(arr[l:r+1])
        ans = min(ans,r-l+1-sm)
        while r < len(arr)-1:
            sm -= arr[l]
            sm += arr[r+1]
            l += 1
            r += 1
            ans = min(ans,r-l+1-sm)
        return ans
        