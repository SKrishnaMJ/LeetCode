class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g=0
        m=0
        p=0
        ans=0
        prefix=[0]
        for t in travel:
            prefix.append(prefix[-1]+t)
        for i, gar in enumerate(garbage):
            ans+=len(gar)
            if 'G' in gar:
                g=i
            if 'M' in gar:
                m=i
            if 'P' in gar:
                p=i
        return ans+prefix[g]+prefix[m]+prefix[p]


        