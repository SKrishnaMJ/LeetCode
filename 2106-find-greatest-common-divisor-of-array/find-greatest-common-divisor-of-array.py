class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        l=[]
        for i in range(1,max(nums)+1):
            if a%i==0 and b%i==0:
                l.append(i)
        return max(l)

        