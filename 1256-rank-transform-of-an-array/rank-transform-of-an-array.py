class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)
        print(nums)
        my_dict = {}
        res=[]
        ctr=1
        for i in range(len(nums)):
            if nums[i] in my_dict:
                continue
            my_dict[nums[i]]=ctr
            ctr+=1
        print(my_dict)
        for j in range(len(arr)):
            res.append(my_dict[arr[j]])
        return res

        