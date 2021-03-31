class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        onesIndex = []
        for i, val in enumerate(s):
            if val == '1':
                onesIndex.append(i)
        total = len(onesIndex)
        if total == 0:
            return ((n - 1) * (n - 2) // 2) % (10 ** 9 + 7)
        if total % 3 != 0:
            return 0
        each = total // 3
        choose1 = onesIndex[each] - onesIndex[each - 1]
        choose2 = onesIndex[each * 2] - onesIndex[each * 2 - 1]
        return choose1 * choose2 % (10 ** 9 + 7)


sol = Solution()
print(sol.numWays('00000000'))
