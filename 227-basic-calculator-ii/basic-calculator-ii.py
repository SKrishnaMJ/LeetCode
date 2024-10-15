class Solution:
    def calculate(self, s: str) -> int:
        sign="+"
        num=0
        stack=[]
        for c in s+'+':
            if c.isdigit():
                num= (num*10) +int(c)
            elif c==' ':
                pass
            else:
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-num)
                elif sign=="*":
                    prev=stack.pop()
                    stack.append((prev*num))
                elif sign=="/":
                    prev=stack.pop()
                    stack.append(int(prev/num))
                num=0
                sign=c
        return sum(stack)