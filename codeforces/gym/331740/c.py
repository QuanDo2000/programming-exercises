t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    count = 0
    l = 0
    r = n - 1
    while l <= r:
        if a[r] >= k:
            r -= 1
            count += 1
        else:
            while a[r] + a[l] < k and l < r:
                l += 1
            if a[r] + a[l] >= k and r != l:
                r -= 1
                l += 1
                count += 1
            else:
                l += 1
    print(count)
