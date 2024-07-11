class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                my_dict[nums[i]]=1
        for k,v in my_dict.items():
            if (v>1):
                return True
        return False
        