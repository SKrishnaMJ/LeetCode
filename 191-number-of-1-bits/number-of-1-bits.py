class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr=0
        a=bin(n).replace("0b", "")
        for i in a:
            if (i=='1'):
                ctr+=1
        return ctr

        