class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ctr=0
        l=[]
        ans=0
        for i in range(len(bank)):
            for j in range(len(bank[i])):
                if bank[i][j]=='1':
                    ctr+=1
            if ctr>0:
                l.append(ctr)
                ctr=0
        
        for i in range(len(l)-1):
            prod=l[i]*l[i+1]
            ans=ans+prod
        return ans
        