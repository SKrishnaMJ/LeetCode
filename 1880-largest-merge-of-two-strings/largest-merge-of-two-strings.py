# class Solution:
#     def largestMerge(self, word1: str, word2: str) -> str:
#         merge=""
#         p1,p2=0,0
#         while(p1<len(word1) and p2<len(word2)):
#             if word1[p1]>word2[p2] or (word1[p1]==word2[p2] and word1[p1:]>word2[p2:]):
#                 merge+=word1[p1]
#                 p1+=1
#             elif word1[p1]<word2[p2] or (word1[p1]==word2[p2] and word1[p1:]<word2[p2:]):
#                 merge+=word2[p2]
#                 p2+=1
#             elif (word1[p1:]==word2[p2:]):
#                 merge+=word1[p1:]+word2[p2:]
#                 p1+=len(word1[p1:])
#                 p2+=len(word2[p2:])
#                 break

#         if p1<len(word1):
#             merge+=word1[p1:]
#         else:
#             merge+=word2[p2:]
#         return merge
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        merge = []
        p1, p2 = 0, 0

        while p1 < len(word1) and p2 < len(word2):
            # Compare substrings lexicographically
            if word1[p1:] > word2[p2:]:
                merge.append(word1[p1])
                p1 += 1
            else:
                merge.append(word2[p2])
                p2 += 1

        # Append the remainder of the strings
        if p1 < len(word1):
            merge.append(word1[p1:])
        else:
            merge.append(word2[p2:])

        return ''.join(merge)
