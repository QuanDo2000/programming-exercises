b, l, d = map(int, input().split())
s = list(map(int, input().split()))
libs = []
books = set()
for i in range(l):
    n, t, m = map(int, input().split())
    v = list(map(int, input().split()))
    v = sorted(v, key=(lambda x: s[x]), reverse=True)[:d]
    libs.append([[i, len(v), t, m, sum(v)], v])

libs = sorted(libs, key=(lambda x: (x[0][4] / x[0][2])), reverse=True)

for i in range(l):
    lib = libs[i]
    ret = [x for x in lib[1] if x not in books]
    ret = sorted(ret, key=(lambda x: s[x]), reverse=True)[:d]
    books.union(ret, books)
    lib[0][1] = len(ret)
    lib[0][4] = sum(ret)
    lib[1] = ret
    libs[i] = lib

libs = sorted(libs, key=(lambda x: (x[0][4] / x[0][2], x[0][3])), reverse=True)

temp = 0
i = 0
for lib in libs:
    i += 1
    temp += lib[0][2]
    if temp >= d:
        break

libs = libs[:i]

with open('outfx.txt', 'w') as f:
    print(i, file=f)
    for lib in libs:
        # print(lib[0], file=f)
        print(lib[0][0], lib[0][1], file=f)
        print(*lib[1], file=f)
