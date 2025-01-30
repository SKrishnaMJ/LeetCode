class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        f,l=1,num
        while f<=l:
            m=(l+f)//2
            mSquared=m*m
            if mSquared==num:
                return True
            elif mSquared>num:
                l=m-1
            else:
                f=m+1
        return False
        