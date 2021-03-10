n = int(input())

mins = []
for i in range(n):
    m, f, w = map(int, input().split())
    mins.append([m, 0, i])
    # -f so that the end of previous wave is sorted before the start of next wave
    mins.append([m + w, -f, i])

mins.sort()

res = 0
hs = [0] * n
for min in mins:
    if min[1] == 0:
        hs[min[2]] = res
    else:
        t = hs[min[2]] - min[1]
        if t > res:
            res = t
print(res)
