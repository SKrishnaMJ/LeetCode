class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        l_arr = [0]*n
        r_arr = [0]*n

        # Creating max left & max right arrays
        for i in range(n):
            j = -i-1
            l_arr[i]=l_wall
            r_arr[j]=r_wall
            # first assign l and r wall to zero and assign l and r wall to the boundary of l and r arr and then compute max values between l, r wall and its corrsesponding height
            l_wall= max(l_wall,height[i])
            r_wall= max(r_wall,height[j])
        summ=0
        for i in range(n):
            pot = min(l_arr[i],r_arr[i])
            # We dont want pot-height to be less than zero (pot is potential)
            summ+= max(0, pot-height[i])
        return summ