class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = dict(Counter(nums))
        # c=-1
        # ans=0
        # for k,v in count.items():
        #     if v>c:
        #         c=v
        #         ans=k
        # return ans
        
        # Optimal solution
        ans,c=0,0
        for num in nums:
            if c==0:
                ans=num
            if ans==num:
                c+=1
            else:
                c-=1
        return ans