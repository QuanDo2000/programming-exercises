c = 10 ** 9 + 7
n, m = map(int, input().split())
res = pow(pow(2, m, c) - 1, n, c)
print(res)
