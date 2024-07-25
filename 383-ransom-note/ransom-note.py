class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ctr=0
        my_dict1=Counter(ransomNote)
        my_dict2=Counter(magazine)
        # print(my_dict1)
        for k,v in my_dict1.items():
            if k not in my_dict2.keys() or v>my_dict2[k]:
                return False
        return True
        #     if k in my_dict2.keys() and v<=my_dict2[k]:
        #         ctr+=1
        # if ctr>0:
        #     return True
        # else:
        #     return False



        