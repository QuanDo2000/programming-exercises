n, p, w, d = map(int, input().split())

for y in range(w):
    temp = p - y * d
    x = temp / w
    if temp >= 0 and temp % w == 0 and x + y <= n:
        print(int(x), y, int(n-x-y))
        exit()
print(-1)
