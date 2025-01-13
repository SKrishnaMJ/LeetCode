class Solution:
    def minimumLength(self, s: str) -> int:
        prev=[s[0]]
        my_dict={}
        for j in range(len(s)):
            my_dict[s[j]]=1+my_dict.get(s[j],0)
        for i in range(1,len(s)):
            if s[i] not in prev:
                prev.append(s[i])
            elif s[i] in prev and s[i] in s[i+1:]:
                my_dict[s[i]]-=2
                prev.remove(s[i])
        return sum(my_dict.values())
        