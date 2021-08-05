n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split()))[1:])

# List of sequence that are non-increasing sorted by first number
f = sorted([e for e in s if e == sorted(e, reverse=True)], key=lambda x: -x[0])
# print(f)

# List of sequence that are non-increasing sorted by last number
l = sorted(f[::], key=lambda x: -x[-1])
# print(l)

# q stores the amount of sequence that can't be combined to get a
# non-increasing sequence
q = ans = 0
for e in l:
    while q < len(f) and e[-1] < f[q][0]:
        q += 1
    ans += len(f) - q

# ans stores the amount of combined sequences that are non-increasing
print(n*n - ans)
