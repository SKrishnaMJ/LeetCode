class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums)==0):
            return 0
        b = sorted(nums)
        ctr=0
        prev=b[0]
        l=[]
        for i in b[1:]:
            if(i-prev == 0):
                continue
            elif(i-prev == 1):
                ctr+=1
                prev=i
            else:
                l.append(ctr)
                ctr=0
                prev=i
        l.append(ctr)
        return (max(l)+1)

        