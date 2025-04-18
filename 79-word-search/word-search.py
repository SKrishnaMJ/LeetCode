class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        sol = []
        visited = [[False]*len(board[0])for _ in range(len(board))]

        def backtrack(i,j):
            if i<0 or i>len(board)-1 or j>len(board[0])-1 or j<0 or visited[i][j]:
                return False

            sol.append(board[i][j])
            visited[i][j]=True

            if ''.join(sol) == word:
                return True
                
            if ''.join(sol) != word[:len(sol)]:
                sol.pop()
                visited[i][j] = False
                return False
            
            if (backtrack(i,j+1) or backtrack(i+1,j) or  backtrack(i,j-1) or backtrack(i-1,j)):
                return True
            
            sol.pop()
            visited[i][j]=False
           
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j):
                    return True

        return False