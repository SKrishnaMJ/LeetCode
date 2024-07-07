class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        my_dict={}
        ans=[]
        res=0
        ctr=0
        for num in nums:
            if num in my_dict:
                my_dict[num]+=1
            else:
                my_dict[num] = 1
        for k,v in my_dict.items():
            ans.append(v)
        maximum = max(ans)
        for i in sorted(ans,reverse=True):
            if i==maximum and maximum==1:
                ctr+=1
            elif i==maximum:
                res+=i
            else:
                continue
        if(ctr==len(ans)):
            return ctr
        else:
            return res

        