class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict={}
        res=''
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=1
            else:
                my_dict[s[i]]+=1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        for k,v in sorted_dict.items():
            res+=(k)*v
        return res
        