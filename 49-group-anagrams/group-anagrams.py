class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            d[key].append(st)
        return list(d.values())
        