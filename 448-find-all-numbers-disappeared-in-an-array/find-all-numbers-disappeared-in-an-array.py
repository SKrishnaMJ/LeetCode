class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        my_dict={}
        res=[]
        for i in range(1,len(nums)+1):
            my_dict[i]=0
        for i in nums:
            my_dict[i]+=1
        for k,v in my_dict.items():
            if v==0:
                res.append(k)
        return res
                
        