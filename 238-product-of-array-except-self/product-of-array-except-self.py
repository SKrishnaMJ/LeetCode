class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod=1
        post_prod=1
        i,j=1,len(nums)-2
        pre,post=[pre_prod],[post_prod]
        ans=[]
        while(i<len(nums) and j>=0):
            pre_prod*=nums[i-1]
            pre.append(pre_prod)
            post_prod*=nums[j+1]
            post.append(post_prod)
            i+=1
            j-=1
        post=post[::-1]
        print(pre)
        print(post)
        for k in range(len(pre)):
            ans.append(pre[k]*post[k])
        return ans



            