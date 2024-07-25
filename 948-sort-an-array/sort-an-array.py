class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l=[]
        def ms(nums):
            if len(nums)>1:
                mid=len(nums)//2
                ls=nums[:mid]
                rs=nums[mid:]
                ms(ls)
                ms(rs)
                i=j=k=0
                while(i<len(ls) and j<len(rs)):
                    if ls[i]<rs[j]:
                        nums[k]=ls[i]
                        i+=1
                    else:
                        nums[k]=rs[j]
                        j+=1
                    k+=1
                while(i<len(ls)):
                    nums[k]=ls[i]
                    i+=1
                    k+=1
                while(j<len(rs)):
                    nums[k]=rs[j]
                    j+=1
                    k+=1
            return nums
        l = ms(nums)
        return l
                

        