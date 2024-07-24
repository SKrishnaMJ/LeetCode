class Solution:
    def reverseWords(self, s: str) -> str:
        res=''
        ans=[]
        result=''
        for ch in s:
            if ch!=" ":
                res=res+ch
            elif ch==" ":
                ans.append(res)
                res=('')
        ans.append(res)
        for i in ans[::-1]:
            if i=='':
                continue
            else:
                result = result+" "+i
        return result[1:]

        