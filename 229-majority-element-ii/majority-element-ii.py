class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict={}
        l=len(nums)
        res=[]
        for i in range(l):
            if nums[i] not in my_dict:
                my_dict[nums[i]]=1
            else:
                my_dict[nums[i]]+=1
        for k,v in my_dict.items():
            if v>l//3:
                res.append(k)
        return res
        