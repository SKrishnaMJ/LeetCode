class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use 9 bcause the board is 9x9 matrix

        # To check unique elements in all rows
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j]!='.':
                    s.add(board[i][j])

        # To check unique elemets in all cols
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i]!='.':
                    s.add(board[j][i])


        # To check unique elements in each box 
        start =[(0,0),(0,3),(0,6),
        (3,0),(3,3), (3,6),
        (6,0), (6,3), (6,6)]

        for i,j in start:
            s=set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in s:
                        return False
                    elif board[row][col]!='.':
                        s.add(board[row][col])
        return True