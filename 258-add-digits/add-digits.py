class Solution:
    def addDigits(self, num: int) -> int:
        res=0
        while(num>9):
            num=str(num)
            for i in range(len(num)):
                res=res+int(num[i])
            num=res
            res=0
        return num
        
        