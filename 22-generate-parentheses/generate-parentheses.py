class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(l,r,s):
            if len(s) == n*2:
                res.append(s)
                return

            if l < n:
                backtrack(l+1, r, s+'(')
            if r<l:
                backtrack(l,r+1,s+')')
            
        res=[]
        backtrack(0,0,'')
        return res

        