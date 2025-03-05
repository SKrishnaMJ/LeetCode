class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = dict(Counter(magazine))
        ran = dict(Counter(ransomNote))
        for i in ransomNote:
            if i not in mag or mag[i]<ran[i]:
                return False
        return True

        