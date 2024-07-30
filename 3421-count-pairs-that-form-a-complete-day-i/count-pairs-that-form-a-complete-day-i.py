class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        l=[]
        for i in range(len(hours)):
            for j in range(i+1, len(hours)):
                if hours[i]%24 == 0 and hours[j]%24 == 0 or (hours[i]+hours[j])%24==0:
                    l.append([i,j])
        return(len(l))

        