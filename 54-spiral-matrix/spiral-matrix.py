class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        i,j=0,0
        UP_WALL = 0
        RIGHT_WALL = len(matrix[0])
        LEFT_WALL = -1
        DOWN_WALL = len(matrix)
        UP, DOWN, LEFT, RIGHT = 0,1,2,3
        direction = RIGHT
        while(len(ans)!=len(matrix)*len(matrix[0])):
            if direction==RIGHT:
                while j<RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                RIGHT_WALL-=1
                direction=DOWN
            elif direction==DOWN:
                while i<DOWN_WALL:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1, j-1
                DOWN_WALL-=1
                direction=LEFT
            elif direction==LEFT:
                while j>LEFT_WALL:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                LEFT_WALL+=1
                direction=UP
            else:
                while i>UP_WALL:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                UP_WALL+=1
                direction=RIGHT
        return ans
        