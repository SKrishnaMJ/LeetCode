class Solution:
    def isHappy(self, n: int) -> bool:
        
        while n>5:
            summ=0
            while n!=0:
                rem = n%10
                n = n//10
                summ+=(rem*rem)
            n = summ
        if n==1:
            return True
        else:
            return False
        