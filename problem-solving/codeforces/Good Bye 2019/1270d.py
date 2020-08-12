n, k = list(map(int, input().strip().split()))
x = []
for i in range(1, k + 2):
    print("? " + ' '.join([str(x) for x in range(1, k + 2) if x != i]))
    a, b = list(map(int, input().strip().split()))
    x.append(b)
z = 0
xx = max(x)
for i in x:
    if (i == xx):
        z += 1
print("! " + str(z))
