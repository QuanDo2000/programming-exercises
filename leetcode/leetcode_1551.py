class Solution:
    def minOperations(self, n: int) -> int:
        half = n // 2
        if n % 2 == 0:
            return int(n / 2 * half)
        else:
            return int((1 + n) / 2 * half)
