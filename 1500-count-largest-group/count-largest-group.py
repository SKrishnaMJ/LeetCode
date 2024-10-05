class Solution:
    def countLargestGroup(self, n: int) -> int:
        ctr=0
        my_dict={}
        for i in range(1,n+1):
            if i not in my_dict:
                my_dict[i]=1
                if sum(map(int,(list(str(i))))) in my_dict:
                    my_dict[sum(map(int,(list(str(i)))))]+=1
        l=list(my_dict.values())
        ans=max(l)
        for i in range(len(l)):
            if l[i]==ans:
                ctr+=1
        return ctr

 
        