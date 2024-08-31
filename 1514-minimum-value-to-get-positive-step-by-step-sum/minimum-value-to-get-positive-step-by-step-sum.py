class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s=1
        flag=1
        val=0
        ctr=0
        while(flag):
            val=s
            for i in range(len(nums)):
                val+=nums[i]
                if val<=0:
                    s+=1
                    val=0
                    break
                else:
                    ctr+=1
                    if ctr==len(nums):
                        flag=0
            ctr=0
        return s


        