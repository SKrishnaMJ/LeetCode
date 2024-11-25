class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1=len(num1)
        l2=len(num2)
        num1=num1[::-1]
        num2=num2[::-1]
        if l1>l2:
            num2= num2 + ('0'*(l1-l2))
        else:
            num1 = num1 + ('0'*(l2-l1))
        i,c=0,0
        ans=''
        while(i<len(num1)):
            if c!=0:
                res=(ord(num1[i])-ord('0'))+(ord(num2[i])-ord('0'))+c
                c=res//10
                res=res%10
            else:
                res = (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0'))
                if res>9:
                    c = res // 10
                    res = res % 10
            ans += str(res)
            res = ''
            i += 1
        if c>0:
            ans+=str(c)
        return ans[::-1]


        