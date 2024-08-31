class Solution:
    def pivotInteger(self, n: int) -> int:
        rightSum=0
        leftSum=0
        l=[]
        for i in range(1, n+1):
            l.append(i)
        for i in range(len(l)):
            leftSum+=l[i]
            for j in range(i,len(l)):
                rightSum+=l[j]
            if leftSum == rightSum:
                return i+1
            else:
                rightSum=0
        return -1
