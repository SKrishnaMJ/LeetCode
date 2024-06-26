class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        my_dict={}
        ans=[]
        res =[]
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in my_dict:
                ans.append(numbers[i])
                ans.append(diff)
            else:
                my_dict[numbers[i]]=1
        res.append(numbers.index(ans[1]) + 1)
        res.append(numbers.index(ans[0])+1)
        if res[0] == res[1]:
            res[1] = res[1] + 1

        return res