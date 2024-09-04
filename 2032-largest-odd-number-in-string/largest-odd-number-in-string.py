class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans=0
        flag=0
        sys.set_int_max_str_digits(100000)
        if int(num[-1])%2!=0:
            return num
        for ch in range(len(num)):
            if int(num[ch])%2!=0:
                flag=ch
                ans=max(ans,int(num[ch]))
        print(flag)
        if ans==0:
            return ""
        elif flag!=0 and int(num[:flag+1])%2!=0:
            return num[:flag+1]
        else:
            return str(ans)

        