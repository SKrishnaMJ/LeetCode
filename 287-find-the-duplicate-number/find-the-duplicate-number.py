class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_dict={}
        for i in range(len(nums)):
            if (nums[i] in my_dict):
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]]=1
        for k,v in my_dict.items():
            if(v>1):
                return k
        