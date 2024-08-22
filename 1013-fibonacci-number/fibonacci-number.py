class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        bp=[0]*(n+1)
        bp[1]=1
        bp[2]=1
        for i in range(3,n+1):
            bp[i]=bp[i-1]+bp[i-2]
        return bp[n]
        