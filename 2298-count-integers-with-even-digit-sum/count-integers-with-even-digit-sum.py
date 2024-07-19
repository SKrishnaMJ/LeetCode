class Solution:
    def countEven(self, num: int) -> int:
        ctr=0
        temp=0
        rem=0
        s=0
        for i in range(num+1):
            if(i<10 and i%2 == 0):
                ctr+=1
            elif(i>9):
                tem=i
                while(tem>0):
                    rem=tem%10
                    tem=tem//10
                    s=s+rem
                if(s%2==0):
                    ctr+=1
                s=0
        return ctr-1

        