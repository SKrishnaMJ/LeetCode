class Solution:
    def reverse(self, x: int) -> int:
        ch=''

        st_x = str(x)
        if(st_x[0]=='-'):
            ch=st_x[0]
        rev_x = st_x[::-1]
        l=len(rev_x)
        if(rev_x[l-1]==ch):
            a = int(rev_x[:l-1])
            ans = a*(-1)

        else:
            ans = int(rev_x)

        if(ans<=(pow(2,31))*-1 or ans>=(pow(2,31)-1)):
            return 0
        return ans

 