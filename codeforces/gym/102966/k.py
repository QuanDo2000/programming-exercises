n, m = map(int, input().split())

b = list(map(int, input().split()))
o = list(map(int, input().split()))

w = 0
i = 0
for j in range(m):
    curr_o = o[j]
    while curr_o > 0 and i < n:
        # print(i, j, curr_o)
        curr_o -= b[i]
        if curr_o < 0:
            w += curr_o + b[i]
            break
        i += 1
    if i == n:
        w += curr_o
print(w)
