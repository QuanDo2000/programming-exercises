q = int(input())
for _ in range(q):
    a, b, c = map(int, input().split())
    s = abs(a - b) + abs(a - c) + abs(b - c)
    print(max(0, s-4))
