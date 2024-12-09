class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        res=0
        l=0
        for r in range(len(s)):
            my_dict[s[r]]=1+my_dict.get(s[r],0)
            while (r-l+1)-max(my_dict.values()) > k:
                my_dict[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res     