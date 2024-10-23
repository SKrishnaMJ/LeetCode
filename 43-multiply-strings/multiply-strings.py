class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_dig(num):
            res=0
            for c in num:
                digit=ord(c)-ord("0")
                res=res*10+digit
            return res
        n1=str_to_dig(num1)
        n2=str_to_dig(num2)
        return str(n1*n2)