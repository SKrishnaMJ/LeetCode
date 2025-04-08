class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0]*n
        indices = deque(range(n))

        for card in deck:
            ind = indices.popleft()
            res[ind] = card
            if indices:
                indices.append(indices.popleft())
        return res
        