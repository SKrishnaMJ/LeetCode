class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans=0
        left=0
        my_dict={'a':0, 'b':0, 'c':0}
        for i in range(len(s)):
            my_dict[s[i]]+=1
            while(my_dict['a'] and my_dict['b'] and my_dict['c']):
                ans+=len(s)-i
                my_dict[s[left]]-=1
                left+=1
        return ans

        