class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Using Montotonic Stack (descending oder)
        t = temperatures
        n = len(t)
        ans = [0]*n
        stk = []
        for i,t in enumerate(t):
            while stk and stk[-1][0]<t:
                stk_t, stk_i = stk.pop()
                ans[stk_i] = i-stk_i
            stk.append((t,i))
        return ans



            
        