class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        ctr=0
        for i in range(len(A)):
            for j in range(0,i+1):
                if B[j] in A[:i+1]:
                    ctr+=1
            c.append(ctr)
            ctr=0
        return c