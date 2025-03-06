class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        i=0
        n=len(height)-1
        while i<n:
        
            ans=max(ans, ((n+1)-(i+1))*min(height[n],height[i]))
            if height[n]>height[i]:
                i+=1
            else:
                n-=1
        return ans
        