class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for k in range(len(matrix)):
        #     i = 0
        #     j = len(matrix[0])-1
        #     while i<=j and target <= matrix[k][j]:
        #         mid = (j+i)//2
        #         if matrix[k][mid]==target:
        #             return True
        #         elif matrix[k][mid] > target:
        #             j = mid-1
        #         else:
        #             i = mid+1
        # return False
        m = len(matrix)
        n = len(matrix[0])
        tot = m*n
        i = 0
        j = tot-1
        while i<=j:
            mid = (i+j)//2
            x = mid//n
            y = mid%n
            ele = matrix[x][y]
            if ele==target:
                return True
            elif target > ele:
                i = mid+1
            else:
                j = mid-1
        return False
            
            
        