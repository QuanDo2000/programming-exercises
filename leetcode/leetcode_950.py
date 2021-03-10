class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        deck = sorted(deck)
        ret_list = []
        while deck:
            if ret_list:
                ret_list.insert(0, ret_list.pop())
            ret_list.insert(0, deck.pop())
        return ret_list


sol = Solution()
ans = sol.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7])
print(ans)
