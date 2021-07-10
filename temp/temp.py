def fact(n):
    if n == 0:
        return 1
    ans = 1
    for i in range(1, n + 1):
        ans *= i
    return ans


n = 13
ans = fact(n)
for i in range(n):
    ans -= fact(i) * fact(n - 1 - i)
print(ans % (1e9 + 9))
