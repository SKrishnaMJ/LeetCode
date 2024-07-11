class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        setx=set()
        ctr=0
        for word in words:
            if word in setx:
                ctr+=1
            else:
                setx.add(word)
                setx.add(word[::-1])
        return ctr

        