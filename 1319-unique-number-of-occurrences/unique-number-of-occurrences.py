class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict={}
        l=[]
        for i in range(len(arr)):
            if arr[i] in my_dict:
                my_dict[arr[i]]+=1
            else:
                my_dict[arr[i]]=1
        for k,v in my_dict.items():
            l.append(v)
        for i in l:
            if(l.count(i)>1):
                return False
        return True
            
        