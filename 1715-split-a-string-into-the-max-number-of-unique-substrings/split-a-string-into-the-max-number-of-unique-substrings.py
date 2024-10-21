class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        setx=set()
        def backtrack(start, setx):
            if start==len(s):
                return 0
            res=0
            for i in range(start+1, len(s)+1):
                sub=s[start:i]
                if sub not in setx:
                    setx.add(sub)
                    res=max(res,1+backtrack(i,setx))
                    setx.remove(sub)
            return res
        return backtrack(0, setx)
        