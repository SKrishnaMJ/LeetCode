class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n<=0):
            return False
        # for i in range((n//2)+1):
        #     if(n==pow(2,i)):
        #         ctr=1
        #         break
        # if(ctr==1):
        #     return True

        
        while(n>1):
            if(n%2==0):
                n=n/2
            else:
                return False
                break
        return True

                
        