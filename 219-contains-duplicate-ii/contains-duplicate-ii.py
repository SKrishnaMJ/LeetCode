class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]]=i
            elif nums[i] in my_dict:
                if abs(my_dict[nums[i]]-i)>k:
                    my_dict[nums[i]]=i
                else:
                    return True
        return False

        