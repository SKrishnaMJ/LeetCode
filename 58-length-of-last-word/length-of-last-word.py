class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        flag =0
        ctr=0
        for i in s[::-1]:
            if (i == " " and flag ==0):
                continue
            elif (i != " "):
                flag = 1
                ctr += 1
            else:
                break
        return ctr

        