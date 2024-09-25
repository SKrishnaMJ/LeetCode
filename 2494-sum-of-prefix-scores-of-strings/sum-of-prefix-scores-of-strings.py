class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # res=[]
        # tot,ans=0,0
        # for word in words:
        #     n=len(word)
        #     while(n!=0):
        #         for i in range(len(words)):
        #             if word[:n] == words[i][:n]:
        #                 tot+=1
        #         n-=1
        #         ans+=tot
        #         tot=0
        #     res.append(ans)
        #     ans=0
        # return res
        k=defaultdict(int)
        ans=[]
        for i in words:
            for j in range(len(i)):
                k[i[0:j+1]]+=1
        for i in words:
            ctr=0
            for j in range(len(i)):
                ctr+=k[i[0:j+1]]
            ans.append(ctr)
        return ans
                