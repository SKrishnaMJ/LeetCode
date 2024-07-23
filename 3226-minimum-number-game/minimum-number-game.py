class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heap=[]
        for i in nums:
            heappush(heap,i)
        print(heap)
        res=[]
        ans=[]
        while(heap):
            for i in range(2):
                res.append(heappop(heap))
            ans=ans+res[::-1]
            res=[]
            
        return ans

        