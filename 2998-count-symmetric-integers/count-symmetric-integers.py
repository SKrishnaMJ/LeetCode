class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
      
        ctr=0

        for i in range(low,high+1):
            preSum = 0
            postSum = 0
            temp=list(str(i))
            if len(temp)%2 != 0:
                continue
            else:
                mid=len(temp)//2
                for j in range(0,mid):
                    preSum=preSum+int(temp[j])
                for k in range(mid,len(temp)):
                    postSum=postSum+int(temp[k])
                if(preSum==postSum):
                    ctr+=1
        return ctr
        