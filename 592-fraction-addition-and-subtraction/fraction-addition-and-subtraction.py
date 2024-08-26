from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        ex=list(expression)
        num=ex[0]
        l=[]
        ans=0
        for i in range(1, len(ex)):
            if ex[i] == "-" or ex[i] == "+":
                l.append(num)
                num=""
                num+=ex[i]
            else:
                num+=ex[i]
        l.append(num)
        for j in range(len(l)):
            ans+=eval(l[j])
        res=str(Fraction(ans).limit_denominator())
        if res in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9", "-1", "-2", "-3", "-4", "-5","6", "-7", "-8", "-9"]:
            return res+"/1"
        return res
        