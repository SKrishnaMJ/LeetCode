class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # f=points[0]
        # flag = 0
        # for i in range(1,len(points)):
        #     if(((points[i][0]-f[0]) == 0) or (points[i][1]-f[1])/(points[i][0]-f[0])  == 1):
        #         flag+=1
        #         f=points[i]
        #     else:
        #         f=points[i]
        # if (flag == 2):
        #     return False
        # else:
        #     return True
        return ((points[0][0]-points[1][0])*(points[0][1]-points[2][1]) != (points[0][0]-points[2][0]) * (points[0][1] - points[1][1]))

            
        