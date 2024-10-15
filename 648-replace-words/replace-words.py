class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dict_set = set(dictionary)
        words=sentence.split()
        res=[]
        for word in words:
            ans=False
            for i in range(1, len(word)+1):
                if word[:i] in dict_set:
                    res.append(word[:i])
                    ans=True
                    break
            if not ans:
                res.append(word)
        return ' '.join(res)

        