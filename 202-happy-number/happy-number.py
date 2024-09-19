class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        ans=0

        while(int(n)>5):
            n=str(n)
            for i in range(len(n)):
                ans+=int(n[i])*int(n[i])
            if ans==1:
                return True
            n=str(ans)
            ans=0
        return False
        