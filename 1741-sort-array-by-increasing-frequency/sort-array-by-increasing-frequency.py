class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq_ele = Counter(nums)
        heap=[]
        for i in freq_ele:
            heappush(heap,(freq_ele[i], -i))
        res=[]
        while(heap):
            a,b = heappop(heap)
            for j in range(a):
                res.append(-b)
        return res

        