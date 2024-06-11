class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        l = []
        for i in nums:
            if (i in my_dict):
                my_dict[i]+=1
            else:
                my_dict[i]=1
        for a,v in my_dict.items():
            heappush(l,(v,a))
            # print(l)
            if(len(l)>k):
                heappop(l)
        ans = []
        while l:
            ans.append(heappop(l)[1])
        return ans
            
