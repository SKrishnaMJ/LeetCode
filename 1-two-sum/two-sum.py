class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            my_dict[nums[i]]=i
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in my_dict and my_dict[diff]!=i:
                return [i, my_dict[diff]]
        