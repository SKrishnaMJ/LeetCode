class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        my_dict = {')':'(',
        '}':'{',
        ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if not stack or stack.pop()!=my_dict[s[i]]:
                    return False
        return True if len(stack)==0 else False
        