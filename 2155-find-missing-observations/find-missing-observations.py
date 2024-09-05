class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        ans=mean*(len(rolls)+n)-sum(rolls)
        if ans > 6*n or ans < n:
            return []
        q,r = divmod(ans, n)
        res=[q]*n
        for i in range(r):
            res[i]+=1
        return res

        # return [q+1]*r + [q]*(n-r)
        
        


        