from bisect import bisect_left


t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    dif = [0] * (n - 1)
    if 1 not in b:
        print(-1)
    elif max(b) >= (2 * n):
        print(-1)
    else:
        ans = [0] * (2 * n)
        base = list(range(1, (n*2)+1))
        for i in range(n):
            ans[i*2] = b[i]
            base.remove(b[i])
        for i in range(n):
            index = bisect_left(base, ans[i*2])
            if index == len(base):
                print(-1)
                break
            ans[i*2+1] = base.pop(index)
        else:
            print(*ans)
