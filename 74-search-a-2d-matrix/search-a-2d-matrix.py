class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for k in range(len(matrix)):
            i = 0
            j = len(matrix[0])-1
            while i<=j and target <= matrix[k][j]:
                mid = (j+i)//2
                if matrix[k][mid]==target:
                    return True
                elif matrix[k][mid] > target:
                    j = mid-1
                else:
                    i = mid+1
        return False

            
        