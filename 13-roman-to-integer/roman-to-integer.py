class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res=0
        n=len(s)
        i=0
        while(i<n):
            if  i<n-1 and my_dict[s[i]] < my_dict[s[i+1]]:
                res+=my_dict[s[i+1]]-my_dict[s[i]]
                i+=2
            else:
                res+=my_dict[s[i]]
                i+=1
        return res


        