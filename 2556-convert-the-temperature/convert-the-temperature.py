class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        l=[]
        k=celsius+273.15
        l.append(k)
        f=(celsius*1.80)+32.00
        l.append(f)
        return l
        