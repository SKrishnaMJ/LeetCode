class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==1:
            return False
        st=[]
        my_dict = {')':'(', '}':'{',']':'['}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                st.append(i)
            else:
                if not st or st.pop()!=my_dict[i]:
                    return False
        if len(st)!=0:
            return False
        else:
            return True

        