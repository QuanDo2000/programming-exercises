t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    b += 1
    print(a * (len(str(b)) - 1))
