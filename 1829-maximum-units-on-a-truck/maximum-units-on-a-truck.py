class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_list=sorted(boxTypes, key=lambda x:x[1], reverse=True)
        ans=0
        for i in range(len(sorted_list)):
            if sorted_list[i][0]<=truckSize:
                ans+=sorted_list[i][0]*sorted_list[i][1]
                truckSize-= sorted_list[i][0]
            else:
                ans+=truckSize*sorted_list[i][1]
                break
        return ans
        
        