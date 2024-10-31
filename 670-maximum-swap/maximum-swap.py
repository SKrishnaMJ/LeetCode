class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(map(int,list(str(num))))
        for i in range(len(n)):
            m = max(n[i:])
            if n[i:].count(m)>1:
                index = len(n[i:])-n[i:][::-1].index(m)-1
            else:
                index = n[i:].index(m)
            if n[i] == m:
                continue
            else:
                temp = n[i]
                n[i] = m
                n[index+i] = temp
                break
        return int(''.join(list(map(str, n))))