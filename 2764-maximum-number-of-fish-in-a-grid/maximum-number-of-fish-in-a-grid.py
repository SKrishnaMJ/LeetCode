class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans,self.res=0,0
        setx=set()
        def dfs(r, c):
            if (r,c) not in setx:
                setx.add((r,c))
            else:
                return 0
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
                return 0
            if grid[r][c]>0:
                self.res+=grid[r][c]
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
            return self.res


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    ans=max(ans, dfs(i,j))
                self.res=0
        return ans