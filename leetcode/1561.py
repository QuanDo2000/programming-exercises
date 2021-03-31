class Solution:
    def maxCoins(self, piles: list) -> int:
        piles = sorted(piles, reverse=True)
        length_3 = len(piles) // 3
        piles = [num for num in piles[1:-length_3:2]]
        return sum(piles)
