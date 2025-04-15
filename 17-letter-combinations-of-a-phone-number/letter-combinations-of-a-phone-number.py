class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        my_dict = {'2':'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs',
                   '8':'tuv', '9':'wxyz'}
        
        res, sol = [], []

        n = len(digits)

        def backtrack(i):
            if i == n:
                res.append(''.join(sol))
                return

            for ch in my_dict[digits[i]]:
                sol.append(ch)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return res




        