class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans=0
        candidate = 0
        for k,v in count.items():
            if v>ans:
                ans=v
                candidate=k
        return candidate
            