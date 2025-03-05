class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count = defaultdict(int)
        my_dict=dict(Counter(target))
        m=float(inf)

        for ch in s:
            if ch in target:
                count[ch]+=1

        for ch in target:
            if ch not in s:
                return 0
            m=min(m, count[ch]//my_dict[ch])
        return m