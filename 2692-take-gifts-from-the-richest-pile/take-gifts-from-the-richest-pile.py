class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            num = max(gifts)
            gifts.remove(num)
            gifts.append(int(num**0.5))
        return sum(gifts)