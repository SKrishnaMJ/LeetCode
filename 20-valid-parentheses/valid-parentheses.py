class Solution(object):
    def isValid(self, s):
        my_dict = {')':'(', ']':'[','}':'{'}
        stack =[]
        for char in s:
            if char in my_dict.values():
                stack.append(char)
            elif char in my_dict.keys():
                if not stack or my_dict[char] != stack.pop():
                    return False
        return not stack
        

        