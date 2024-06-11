class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convBinary(binaryStr):
            p=len(binaryStr)-1
            sum=0
            for i in binaryStr:
                if(i=='0'):
                    p=p-1
                elif(i=='1'):
                    sum = sum + pow(2,p)
                    p=p-1
            return sum
        
        sumInt = convBinary(a) + convBinary(b)
        sumBin = bin(sumInt)
        return (sumBin[2:])
        