class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = dict(Counter(nums))
        for val in x.values():
            if val>=2:
                return True
        return False
        