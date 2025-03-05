class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = defaultdict(int)
        s = "balloon"

        for ch in text:
            if ch in s:
                count[ch]+=1
        
        for ch in s:
            if ch not in text:
                return 0
        return min(count['b'], count['o']//2, count['a'], count['l']//2, count['n'])

        