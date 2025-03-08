class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        capacity.sort(reverse=True)
        c=0
        for i in capacity:
            if tot<=0:
                break
            tot-=i
            c+=1
            
        return c
        