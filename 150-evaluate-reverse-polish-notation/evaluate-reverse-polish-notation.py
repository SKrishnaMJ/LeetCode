class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != "+" and i != "-" and i != "/" and i != "*":
                stack.append(i)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == "+":
                    ans = int(op1) + int(op2)
                    stack.append(str(ans))
                elif i == "-":
                    ans = int(op1) - int(op2)
                    stack.append(str(ans))
                elif i == "/":
                    ans = math.trunc(int(op1) / int(op2))
                    stack.append(str(ans))
                else:
                    ans = int(op1) * int(op2)
                    stack.append(str(ans))
                
        return int(stack[0])
        