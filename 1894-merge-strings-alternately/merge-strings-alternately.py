class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merged=''
        # n=len(word1)
        # m=len(word2)
        # for i in range(min(n,m)):
        #     merged+=word1[i]+word2[i]
        # if m>n:
        #     return merged+word2[n:]
        # else:
        #     return merged+word1[m:]
        m,n = len(word1), len(word2)
        a,b = 0,0
        res = []
        word = 1
        while(a<m and b<n):
            if word == 1:
                res.append(word1[a])
                a+=1
                word=2
            else:
                
                res.append(word2[b])
                b+=1
                word=1
        while(a<m):
            res.append(word1[a])
            a+=1
        while(b<n):
            res.append(word2[b])
            b+=1
        return ''.join(res)
        

        