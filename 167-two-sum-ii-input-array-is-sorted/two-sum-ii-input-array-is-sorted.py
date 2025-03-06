class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            d[numbers[i]]=i+1
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in d and d[diff]!=i+1:
                return [i+1, d[diff]]
        