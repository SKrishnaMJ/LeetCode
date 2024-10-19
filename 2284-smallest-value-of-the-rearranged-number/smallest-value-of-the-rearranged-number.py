class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return num
        if num<0:
            n=num*-1
            n = str(n)
        else:   n = str(num)
        n=list(map(int, n))
        n.sort()
        res=''
        ans=[]
        z=0
        for i in range(len(n)):
            if n[i]==0:
                z+=1
            else:
                res+=str(n[i])
        res=list(res)
        if num>0 and z>0:
            ans.append(res[0])
            ans.append('0'*z)
            for i in range(1,len(res)):
                ans.append(res[i])
            return int(''.join(ans))
        if num<0 and z>0:
            ans=res[::-1]
            ans.append('0'*z)
            return -1*int(''.join(ans))
        return int(''.join(res)) if num>0 else -1*int(''.join(res[::-1]))
