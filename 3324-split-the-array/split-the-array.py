class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        my_dict = Counter(nums)
        for k,v in my_dict.items():
            if v>2:
                return False
        return True        