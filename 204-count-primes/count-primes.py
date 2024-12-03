class Solution:
    def countPrimes(self, n: int) -> int:
        #Using Sieve of Eratostenes
        res=0
        ans=["T"] * n
        for i in range(2, int(n**0.5)+1):
            if ans[i]=="T":
                for j in range(i*i,n,i):
                    ans[j]="F"
        for k in range(2,n):
            if ans[k]=="T":
                res+=1
        return res
        