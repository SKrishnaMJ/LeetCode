class Solution:
    def findComplement(self, num: int) -> int:
        n=bin(num)
        c=''
        ans=0
        for i in n[2:]:
            if i=='1':
                c+='0'
            else:
                c+='1'
        c=c[::-1]
        for i in range(len(c)):
            if c[i]=='1':
                ans+=pow(2,i)
        return ans