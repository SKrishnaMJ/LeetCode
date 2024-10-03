class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        rem = tot%p
        if rem==0:
            return 0
        n = len(nums)
        res = n
        psum = 0
        my_dict = {0:-1}

        for i in range(n):
            psum += nums[i]
            r = psum%p
            req_rem = (r-rem+p)%p

            if req_rem in my_dict:
                # Why this step ? gotta fiigure out
                res = min(res,i-my_dict[req_rem]) 

            my_dict[r] = i
        
        return res if res<n else -1

