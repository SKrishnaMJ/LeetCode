class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans=[]
        z=dict(zip(heights, names))
        res = dict(sorted(z.items(), key=lambda item: item[0], reverse=True))
        for k,v in res.items():
            ans.append(v)
        return ans



        
        