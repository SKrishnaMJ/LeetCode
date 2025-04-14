class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
                return
            
            for k in range(n):
                if nums[k] not in sol:
                    sol.append(nums[k])
                    backtrack()
                    sol.pop()
            
        backtrack()
        return res
            
        