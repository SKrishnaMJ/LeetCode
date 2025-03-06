class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # d={}
        # for i in range(len(numbers)):
        #     d[numbers[i]]=i+1
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in d and d[diff]!=i+1:
        #         return [i+1, d[diff]]
        f=0
        l=len(numbers)-1
        while f<l:
            if target - numbers[f] == numbers[l]:
                return [f+1, l+1]
            elif target - numbers[f] > numbers[l]:
                f+=1
            else:
                l-=1