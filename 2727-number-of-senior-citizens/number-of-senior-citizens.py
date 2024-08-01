class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ctr=0
        for age in details:
            if(int(age[11:13])>60):
                ctr+=1
        return ctr
        