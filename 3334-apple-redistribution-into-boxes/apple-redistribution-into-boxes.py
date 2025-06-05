class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        tot = sum(apple)
        capacity.sort(reverse=True)
        box=0
        for c in capacity:
            if tot>0:
                tot-=c
                box+=1
        return box

        