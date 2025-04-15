class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(start, summ):
            if summ == target:
                res.append(sol[:])
                return
            if summ>target:
                return
            
            for i in range(start, n):
                
                sol.append(candidates[i])
                backtrack(i, summ+candidates[i])
                sol.pop()

        backtrack(0,0)
        return res
            
