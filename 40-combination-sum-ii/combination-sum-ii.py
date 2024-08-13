class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        
        def backtrack(start, path, target):
            if target==0:
                res.append(list(path))
                return


            for i in range(start, len(candidates)):
                if candidates[i]>target:
                    continue
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, target-candidates[i])
                path.pop()
        backtrack(0,[], target)
        return res
        


        