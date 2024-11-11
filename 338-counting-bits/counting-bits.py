class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            b=bin(i)[2:]
            l.append(b.count('1'))
        return list(map(int,l))
        