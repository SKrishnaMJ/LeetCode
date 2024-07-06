class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        con=0
        for word in words:
            count = 0
            if len(word) == 1 and word in allowed:
                con+=1
                continue
            for ch in word:
                if ch not in allowed:
                    count = 0
                    break
                else:
                    count+=1
            if count>0:
                con+=1
        return con

        