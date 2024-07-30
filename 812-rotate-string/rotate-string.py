class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a=list(s)
        b=list(goal)
        for i in range(len(s)):
            if a != b:
                ele=a.pop()
                a.insert(0,ele)
            elif(a==b):
                return True
        return False

        