import sys
import time


DEBUG = False


# def rec(k):
#     dp = [[0, []] for i in range(k + 1)]
#     j = 1
#     t = 1
#     dp[0] = [0, []]

#     for i in range(1, k + 1):
#         dp[i] = [sys.maxsize, []]
#         while j <= i:
#             if DEBUG:
#                 print(i, j, t, dp[i])

#             if j == i:
#                 dp[i][0] = 1
#                 dp[i][1] = [t]
#             elif (dp[i][0] > dp[i - j][0]):
#                 dp[i][0] = dp[i - j][0] + 1
#                 dp[i][1] = dp[i - j][1][:]
#                 dp[i][1].append(t)
#             t += 1
#             j = t ** 3
#         t = j = 1

#     if DEBUG:
#         print(dp)

#     return dp[k]


n = int(input())

ans = (n - (n % 6) ** 3) // 6

if DEBUG:
    print(ans)

print(5)
print(ans + 1, ans - 1, -ans, -ans, (n % 6))
