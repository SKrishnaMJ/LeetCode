# class Solution:
#     def maximumTripletValue(self, nums: List[int]) -> int:
#         # ans = float("-inf")
#         # for i in range(len(nums)):
#         #     j=i+1
#         #     k=len(nums)-1
#         #     while j<k:
#         #         res = (nums[i]-nums[j])*nums[k]
#         #         ans = max(ans, res)
#         #         if nums[j]>=nums[k]:
#         #             k-=1
#         #         else:
#         #             j+=1
#         # return ans if ans>=0 else 0
#         ans = float("-inf")
#         for i in range(len(nums)-2):
#             for j in range(i+1,len(nums)-1):
#                 for k in range(j+1,len(nums)):
#                     res = (nums[i]-nums[j])*nums[k]
#                     ans = max(ans, res)
#         return ans if ans>=0 else 0
                    
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        hi, d, ans = 0, 0, 0
        for x in nums:
            ans = max(ans, d*x)
            d = max(hi - x, d)
            hi = max(hi, x)
        return ans