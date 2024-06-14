class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict={}
        ans=0
        for i in nums:
            if (i in my_dict.keys()):
                my_dict[i]+=1
            else:
                my_dict[i]=1
        for k,v in my_dict.items():
            if(v==1):
                ans=k
                break
        return ans
            

        