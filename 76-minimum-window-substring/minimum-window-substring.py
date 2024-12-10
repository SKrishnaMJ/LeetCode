class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" or len(t)>len(s): return ""
        l=0
        ans=[-1,-1]
        lenAns=float("inf")
        dictT, win = {}, {}
        for i in t:
            dictT[i]=1+dictT.get(i,0)
        winLen, dictLen = 0, len(dictT)
        for r in range(len(s)):
            ch=s[r]
            win[ch]=1+win.get(ch,0)
            if ch in dictT and win[ch]==dictT[ch]:
                winLen+=1
            
            while winLen==dictLen:
                if (r-l+1) < lenAns:
                    ans=[l,r]
                    lenAns=(r-l+1)
                win[s[l]]-=1
                if s[l] in dictT and dictT[s[l]]>win[s[l]]:
                    winLen-=1
                l+=1
        return s[ans[0]:ans[1]+1] if lenAns!=float("inf") else ""