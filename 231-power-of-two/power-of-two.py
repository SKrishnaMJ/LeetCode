class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if(n<=0):
        #     return False
        # while(n>1):
        #     if(n%2==0):
        #         n=n/2
        #     else:
        #         return False
        #         break
        # return True
        return n>0 and (n&(n-1)==0)