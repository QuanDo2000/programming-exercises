t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(1, n):
        while d >= i and a[i] > 0:
            d -= i
            a[0] += 1
            a[i] -= 1
    print(a[0])
