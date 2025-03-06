class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            l,h = i+1,n-1
            while l<h:
                summ = nums[i]+nums[l]+nums[h]
                if summ==0:
                    ans.append([nums[i],nums[l],nums[h]])
                    l+=1
                    h-=1
                    while l<h and nums[l-1]==nums[l]:
                        l+=1
                    while l<h and nums[h]==nums[h+1]:
                        h-=1
                elif summ>0:
                    h-=1
                else:
                    l+=1
        return ans

        