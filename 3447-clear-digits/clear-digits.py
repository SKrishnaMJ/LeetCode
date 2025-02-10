class Solution:
    def clearDigits(self, s: str) -> str:
        st=[]
        i=0
        while(i<len(s)):
            if s[i].isdigit():
                st.pop()
                i+=1
            else:
                st.append(s[i])
                i+=1
        return ''.join(st)
        