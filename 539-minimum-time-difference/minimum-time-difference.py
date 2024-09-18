class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ans = float("inf")
        res = []
        
        # Convert time points to minutes
        for time in timePoints:
            t = time.split(":")
            minutes = int(t[0]) * 60 + int(t[1])
            res.append(minutes)
        
        # Sort the list of times in ascending order
        res.sort()
        
        # Check adjacent time differences
        for i in range(1, len(res)):
            ans = min(ans, res[i] - res[i - 1])
        
        # Circular difference between last and first time points
        circular_diff = 24 * 60 - res[-1] + res[0]
        ans = min(ans, circular_diff)
        
        return ans

        