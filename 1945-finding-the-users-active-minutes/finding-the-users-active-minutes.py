class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        my_dict={}
        ans=[0]*k
        for i,j in logs:
            if i not in my_dict:
                my_dict[i]=set()
            my_dict[i].add(j)
        for k,v in my_dict.items():
            ans[len(v)-1]+=1
        return ans
    
        