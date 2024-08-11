class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        ctr = 0

        if len(password) < 8:
            return False
        if any(char.islower() for char in password):
            ctr += 1
        if any(char.isupper() for char in password):
            ctr += 1
        if any(char.isdigit() for char in password):
            ctr += 1
        if re.findall(r'\W', password):
            ctr += 1
        print(ctr)
        for i in range(len(password) - 1):
            if password[i] == password[i + 1]:
                ctr=0
                break
        print(ctr)
        if ctr == 4:
            return True
        
    
        