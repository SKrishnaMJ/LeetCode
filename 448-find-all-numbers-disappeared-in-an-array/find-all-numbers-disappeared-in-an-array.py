class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        setx=set(range(1,len(nums)+1))
        for i in nums:
            if i in setx:
                setx.remove(i)
        return setx
  
                
        