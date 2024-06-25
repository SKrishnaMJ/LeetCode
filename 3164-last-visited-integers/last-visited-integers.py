class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k=0
        prev=-1
        for i in nums:
            if (i>0):
                seen = [i] + seen
            elif(i == -1):
                if(prev==-1):
                    k+=1
                else:
                    k=1
                if(k <= len(seen)):
                    ans.append(seen[k-1])
                else:
                    ans.append(-1)
            prev=i
        return ans
        