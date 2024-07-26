class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans=0
        my_dict={}
        for i in range(len(arr)):
            if arr[i] in my_dict:
                my_dict[arr[i]]+=1
            else:
                my_dict[arr[i]]=1
        for k,v in my_dict.items():
            if(k==v):
                ans=max(ans,k)
        if ans==0:
            return -1
        else:
            return ans
        # for i in arr:
        #     if i == arr.count(i):
        #         ans=max(ans, i)
  
        f


        