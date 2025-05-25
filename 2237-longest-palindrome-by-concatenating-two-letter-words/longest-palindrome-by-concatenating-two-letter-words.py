class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        my_dict = dict(Counter(words))
        print(my_dict)
        pairs, central = 0,0
        for word, cnt in my_dict.items():
            rev = word[::-1]

            if word==rev:
                pairs+=cnt//2
                if cnt%2:
                    central=1
            else:
                if rev in my_dict and rev<word:
                    pairs+=min(cnt, my_dict[rev])
        return pairs*4 + central*2



        