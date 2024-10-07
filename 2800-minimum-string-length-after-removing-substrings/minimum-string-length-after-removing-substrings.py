class Solution:
    def minLength(self, s: str) -> int:
        while("AB" in s or "CD" in s):
            t = list(s)
            i = 0
            while i < len(t) - 1:
                if (t[i] == 'A' and t[i+1] == 'B') or (t[i] == 'C' and t[i+1] == 'D'):
                    t.pop(i)
                    t.pop(i)  # The next element is at the same index after popping the first
                else:
                    i += 1
            s = ''.join(t)
        return len(s)
        