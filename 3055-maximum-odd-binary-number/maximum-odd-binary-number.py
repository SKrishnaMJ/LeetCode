class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n=len(s)
        i=s.count('1')
        # if i==1:
        #     return '001'
        ans=''
        for j in range(i-1):
            ans+='1'
        z=n-len(ans)-1
        for k in range(z):
            ans+='0'
        return ans+'1'
        

        