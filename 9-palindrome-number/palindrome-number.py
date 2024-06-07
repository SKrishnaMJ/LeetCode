class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev=0
        while(temp>0):
            rem = temp%10
            temp=temp/10
            rev=(rev*10)+rem
        if(rev==x):
            return True
        else:
            return False

        