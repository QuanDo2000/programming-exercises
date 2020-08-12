# def zero(num):
#     ret = 0
#     for char in str(num)[::-1]:
#         if char != '0':
#             break
#         ret += 1
#     return ret


# def count(num, m):
#     ret = 0
#     while num % m == 0:
#         ret += 1
#         num //= m
#     return ret


# def compare(a, b):
#     a2 = count(a, 2)
#     a5 = count(a, 5)
#     b2 = count(b, 2)
#     b5 = count(b, 5)
#     if a2 < b2 or a5 < b5:
#         return 1
#     else:
#         return 0


n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))

dp2 = [[0 for _ in range(n)] for __ in range(n)]
dp5 = [[0 for _ in range(n)] for __ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if (m[i][j] == 0):
            ans = 1
            path = 'R' * j + 'D' * i + 'R' * (n - 1 - j) + 'D' * (n - 1 - i)
            m[i][j] = 10
for i in range(n):
    for j in range(n):
        x = m[i][j]
        while x % 2 == 0 and x > 0:
            dp2[i][j] += 1
            x //= 2
        while x % 5 == 0 and x > 0:
            dp5[i][j] += 1
            x //= 5

for i in range(1, n):
    dp2[i][0] += dp2[i-1][0]
    dp2[0][i] += dp2[0][i-1]
    dp5[i][0] += dp5[i-1][0]
    dp5[0][i] += dp5[0][i-1]
for i in range(1, n):
    for j in range(1, n):
        dp2[i][j] += min(dp2[i-1][j], dp2[i][j-1])
        dp5[i][j] += min(dp5[i-1][j], dp5[i][j-1])
if dp2[-1][-1] < dp5[-1][-1]:
    dp = dp2
else:
    dp = dp5
if ans == 1 and dp[-1][-1]:
    print(ans)
    print(path)
else:
    i, j = n - 1, n - 1
    path = ''
    while i or j:
        if not i:
            path += 'R'
            j -= 1
        elif not j:
            path += 'D'
            i -= 1
        else:
            if dp[i-1][j] < dp[i][j-1]:
                path += 'D'
                i -= 1
            else:
                path += 'R'
                j -= 1
    path = path[::-1]
    print(dp[-1][-1])
    print(path)

# dp = []
# for i in range(n):
#     dp.append([])
#     for j in range(n):
#         dp[i].append(['', 1])
# for i in range(n):
#     for j in range(n):
#         if j == 0 and i == 0:
#             dp[i][j][1] = m[i][j]
#         elif j == 0:
#             dp[i][j][1] = dp[i-1][j][1] * m[i][j]
#             dp[i][j][0] = dp[i-1][j][0] + 'D'
#         elif i == 0:
#             dp[i][j][1] = dp[i][j-1][1] * m[i][j]
#             dp[i][j][0] = dp[i][j-1][0] + 'R'
#         else:
#             down = dp[i-1][j][1] * m[i][j]
#             right = dp[i][j-1][1] * m[i][j]
#             # print(right, down, count(right, 2), count(
#             #     right, 5), count(down, 2), count(down, 5))
#             if compare(right, down) and zero(right) <= zero(down):
#                 dp[i][j][1] = right
#                 dp[i][j][0] = dp[i][j-1][0] + 'R'
#             else:
#                 dp[i][j][1] = down
#                 dp[i][j][0] = dp[i-1][j][0] + 'D'
# for i in range(n):
#     print(dp[i])
# print(zero(dp[-1][-1][1]))
# print(dp[-1][-1][0])
