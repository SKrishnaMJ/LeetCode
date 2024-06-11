class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)-1
        sum = 1
        for i in digits:

            sum = sum +(i*(pow(10,l)))
            l =l-1
        num = list(map(int, str(sum)))
        return num

        