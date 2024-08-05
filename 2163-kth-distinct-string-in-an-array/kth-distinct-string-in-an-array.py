class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # if(k>len(arr)-1):
        #     return ""
        my_dict={}
        l=[]
        ctr=0
        for i in range(len(arr)):
            if arr[i] not in my_dict:
                my_dict[arr[i]]=1
            else:
                my_dict[arr[i]]+=1
        for key,v in my_dict.items():
            if(v==1):
                ctr+=1
                l.append(key)
        if (ctr>=k):
            return l[k-1]
        else:
            return ""

        