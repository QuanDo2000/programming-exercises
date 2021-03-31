x = list(map(int, input().split()))
x.sort(reverse=True)
a, b, c = x[0] - x[1], x[0] - x[2], x[0] - x[3]
print(a, b, c)
