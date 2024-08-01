class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ctr=0
        dict1=Counter(s)
        dict2=Counter(t)
        for k,v in dict1.items():
            if k not in dict2.keys():
                ctr+=v
            elif k in dict2.keys() and v>dict2[k]:
                ctr+=(v-dict2[k])
        return ctr

        