class Solution:
    def hammingWeight(self, n: int) -> int:
        # ctr=0
        # a=bin(n).replace("0b", "")
        # for i in a:
        #     if (i=='1'):
        #         ctr+=1
        # return ctr
        res=0
        while n:
            res+=n%2
            n=n>>1

        return res

        