class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=sorted(score, reverse=True)
        my_dict={}
        for i in range(len(score)):
            if i==0:
                my_dict[l[i]]="Gold Medal"
            elif i==1:
                my_dict[l[i]]="Silver Medal"
            elif i==2:
                my_dict[l[i]]="Bronze Medal"
            else:
                my_dict[l[i]]=str(i+1)
            
        ans=[]
        for i in score:
            ans.append(my_dict[i])
        return ans
            
        

        