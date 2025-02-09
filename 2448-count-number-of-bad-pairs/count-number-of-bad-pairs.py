class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        total_pairs=(n*(n-1)//2)
        my_dict=defaultdict(int)
        gp=0
        for i in range(n):
            val=nums[i]-i
            gp+=my_dict[val]
            my_dict[val]+=1
        return total_pairs-gp
        