class Solution(object):
    def romanToInt(self, s):
        my_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev = 0
        total = 0
        for i in reversed(s):
            val = my_dict[i]
            if(val<prev):
                total-=val
            else:
                total+=val
            prev=val
        return total


        
        