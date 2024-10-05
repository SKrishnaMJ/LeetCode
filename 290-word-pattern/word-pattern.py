class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        my_dict={}
        p=list(pattern)
        s=list(s.split(" "))
        if len(s)!=len(p):
            return False
        for i in range(len(p)):
            if p[i] not in my_dict and s[i] not in list(my_dict.values()):
                my_dict[p[i]]=s[i]
            elif p[i] not in my_dict and s[i] in list(my_dict.values()) or p[i] in my_dict and my_dict[p[i]]!=s[i]:
                return False
        return True

        