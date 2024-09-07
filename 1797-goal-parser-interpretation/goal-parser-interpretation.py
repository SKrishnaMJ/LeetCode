class Solution:
    def interpret(self, command: str) -> str:
        res=''
        for ch in range(len(command)):
            if command[ch] == '(' and command[ch+1] == 'a':
                res+='al'
            elif command[ch] == '(' and command[ch+1] == ')':
                res+='o'
            elif command[ch] == 'G':
                res+='G'
        return res
        