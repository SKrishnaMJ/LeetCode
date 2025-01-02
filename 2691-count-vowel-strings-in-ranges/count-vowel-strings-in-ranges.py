class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        res,ans=[],[]
        for i in words:
            if i[0] in vowel and i[-1] in vowel:
                res.append(1)
            else:
                res.append(0)
        prefix_sum = [0]*(len(res)+1)
        for k in range(len(res)):
            prefix_sum[k+1]=prefix_sum[k]+res[k]
        for l,r in queries:
            ans.append(prefix_sum[r+1] - prefix_sum[l])
        return ans

        