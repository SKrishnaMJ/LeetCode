class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=0
        for i in arr:
            if i == arr.count(i):
                ans=max(ans, i)
        if ans==0:
            return -1
        else:
            return ans

        