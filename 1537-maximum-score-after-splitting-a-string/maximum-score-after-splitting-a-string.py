class Solution:
    def maxScore(self, s: str) -> int:
        li=[]
        r=''
        l=''
        for i in range(len(s)-1):
            l=l+s[i]
            r=r+s[i+1:]
            ans=l.count('0')+r.count('1')
            li.append(ans)
            r=''
        return max(li)


        