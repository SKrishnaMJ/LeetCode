class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=''.join(sorted(list(s1)))
        for i in range(len(s2)):
            r=''.join(sorted(s2[i:i+len(l)]))
            if l==r:
                return True
            else:
                continue
        return False

        