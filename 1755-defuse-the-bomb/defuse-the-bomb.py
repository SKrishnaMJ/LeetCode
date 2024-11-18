class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        ans=[]
        ext_code = code*2
        if k==0:
            return [0]*len(code)
        elif k>0:
            for i in range(n):
                s=sum(ext_code[i+1:i+1+k])
                ans.append(s)
        else:
            k=abs(k)
            for i in range(n):
                s=sum(ext_code[i+n-k:i+n])
                ans.append(s)
        return ans
        