class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ctr=0
        for i in range(len(heights)):
            if heights[i] != sorted(heights)[i]:
                ctr+=1
        return ctr
        