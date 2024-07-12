class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        m=[]
        for ch in s:
            if ch == ')':
                for i in l[::-1]:
                    if i == '(':
                        l.pop()
                        m.reverse()
                        while m:
                            l.append(m.pop())
                        break
                    else:
                        m.append(l.pop())
                # m=m+l.pop()
            else:
                l.append(ch)
        return "".join(l)

        