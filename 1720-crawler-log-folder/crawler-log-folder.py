class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ctr=0
        for log in logs:
            if re.match(r"[A-Za-z0-9]+/", log):
                ctr+=1
            elif re.match(r"\../", log):
                ctr-=1
                if(ctr<0):
                    ctr=0
            else:
                continue
        if(ctr<0):
            return 0
        else:
            return ctr
        