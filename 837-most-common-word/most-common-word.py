# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         l=paragraph.lower().split(" ")
#         my_dict={}
#         for i in range(len(l)):
#             if '!' in l[i] or '?' in l[i] or "'" in l[i] or ',' in l[i] or ';' in l[i] or '.' in l[i]:
#                 l[i]=l[i][0:len(l[i])-1]
#         for j in range(len(l)):
#             my_dict[l[j]]=1+my_dict.get(l[j],0)
#         sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#         for ban in banned:
#             if ban in sorted_dict.keys():
#                 sorted_dict.pop(ban)
#         return list(sorted_dict.keys())[0]

from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Convert paragraph to lowercase and replace non-alphanumeric characters with spaces
        words = re.findall(r'\w+', paragraph.lower())

        # Count frequency of words
        word_count = Counter(words)

        # Remove banned words from the dictionary
        for ban in banned:
            if ban in word_count:
                del word_count[ban]

        # Return the most common word after filtering
        return max(word_count, key=word_count.get)

