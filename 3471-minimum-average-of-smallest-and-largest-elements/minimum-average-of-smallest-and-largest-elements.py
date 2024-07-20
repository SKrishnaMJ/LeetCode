class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        l=[]
        asc=sorted(nums)
        desc=sorted(nums, reverse=True)
        for i in range(len(nums)//2):
            maxNum = asc.pop()
            minNum = desc.pop()
            avgNum = (maxNum+minNum)/2
            l.append(avgNum)
        return min(l)

        