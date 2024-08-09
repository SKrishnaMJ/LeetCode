class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        ctr=1
        res=[]
        for i in range(len(l)):
            ans=sorted(nums[l[i]:r[i]+1])
            diff=abs(ans[0]-ans[1])
            for j in range(len(ans)-1):
                if diff == abs(ans[j] - ans[j+1]):
                    ctr+=1
            if ctr==len(ans):
                res.append(True)
            else:
                res.append(False)
            ctr=1
        return res




        