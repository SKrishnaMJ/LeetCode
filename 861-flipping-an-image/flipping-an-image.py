class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        ans=[]
        for i in image:
            for j in i[::-1]:
                if j==0:
                    ans.append(1)
                else:
                    ans.append(0)

            res.append(ans)
            ans=[]
        return res
        