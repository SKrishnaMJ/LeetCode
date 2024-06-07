class Solution(object):
    def scoreOfString(self, s):
        i=0
        sum=0
        while (i <= (len(s)-2)):
            sum = sum + abs(ord(s[i]) - ord(s[i+1]))
            i+=1
        return sum
        


        