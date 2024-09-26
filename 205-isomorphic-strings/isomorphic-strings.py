class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        my_dict={}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]]=t[i]
            elif s[i] in my_dict and my_dict[s[i]]!=t[i]:
                return False
        l=list(my_dict.values())
        for i in range(len(l)):
            if l.count(l[i])>1:
                return False
        return True