class Solution:
    def partitionLabels(self, S: str) -> list:

        ends = {char: idx for idx, char in enumerate(S)}
        l, r = 0, 0

        ret = []
        for idx, char in enumerate(S):
            r = max(r, ends[char])
            if idx == r:
                ret.append(r - l + 1)
                l = idx + 1

        return ret
