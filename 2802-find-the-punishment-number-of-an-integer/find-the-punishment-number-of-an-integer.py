class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans=0

        def func(sq, num):
            if sq==num:
                return True
            if sq==0:
                return num == 0
            for k in (10,100,1000):
                if func(sq//k, num-sq%k):
                    return True
            return False
        for i in range(1,n+1):
            if func(sq:=i*i, i):
                ans+=sq
        return ans