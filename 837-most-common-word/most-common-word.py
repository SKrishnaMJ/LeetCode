class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    
        words = re.findall(r'\w+', paragraph.lower())
        word_count = Counter(words)

        
        for ban in banned:
            if ban in word_count:
                del word_count[ban]

        return max(word_count, key=word_count.get)

