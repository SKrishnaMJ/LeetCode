class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res=[]
        minDiff=arr[1]-arr[0]
        for i in range(len(arr)-1):
            minAbsdiff = abs(arr[i+1]-arr[i])

            if(minAbsdiff<minDiff):
                res.clear()
                minDiff=minAbsdiff
                res.append([arr[i],arr[i+1]])
            elif(minAbsdiff==minDiff):
                res.append([arr[i],arr[i+1]])
        return res


        