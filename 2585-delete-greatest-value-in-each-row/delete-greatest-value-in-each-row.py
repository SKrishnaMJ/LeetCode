class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        l=[]
        ans=0
        while grid:
            for rows in grid:
                if rows:
                    m=max(rows)
                    l.append(m)
                    rows.remove(m)
            ans+=max(l)
            l=[]
            grid = [row for row in grid if row]
        return ans

        