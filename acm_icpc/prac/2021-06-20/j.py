MAX_N = 10 ** 4 + 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0 for i in range(MAX_N)]
    for num in a:
        d[num] += 1
    ans = 0
    for idx in range(MAX_N - 1):
        temp = d[idx] + d[idx + 1]
        if temp > ans:
            ans = temp
    print(ans)
