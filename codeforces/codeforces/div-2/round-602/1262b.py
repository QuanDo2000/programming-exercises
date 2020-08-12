def main():
    n = int(input())
    q = list(map(int, input().split()))
    for i in range(1, n+1):
        if q[i-1] < i:
            print(-1)
            return
    app = [0] * n
    ans = [0] * n
    ans[0] = q[0]
    app[q[0] - 1] = 1
    for i in range(1, n):
        if q[i] > q[i-1]:
            ans[i] = q[i]
            app[q[i] - 1] = 1
    num = []
    for i in range(n):
        if app[i] == 0:
            num.append(i+1)
    for i in range(n):
        if ans[i] == 0:
            ans[i] = num.pop(0)
    print(*ans)


t = int(input())
for _ in range(t):
    main()
