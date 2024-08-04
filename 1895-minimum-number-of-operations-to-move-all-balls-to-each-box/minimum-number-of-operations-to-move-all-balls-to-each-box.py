class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ctr=0
        l=[]
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i==j:
                    continue
                if boxes[j]=='1':
                    ctr+=abs(j-i)
            l.append(ctr)
            ctr=0
        return l

        