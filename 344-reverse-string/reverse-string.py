class Solution:
    def reverseString(self, s: List[str]) -> None:

        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(len(s)-1, -1, -1):
            s.append(s[i])
            s.pop(i)

        