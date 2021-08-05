n = int(input())
x, y = [], []
for _ in range(n):
    a, b = map(int, input().split())
    if a not in x:
        x.append(a)
    if b not in y:
        y.append(b)
print(min(len(x), len(y)))
