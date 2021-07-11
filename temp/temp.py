from itertools import permutations


def check(perm):
    flag = True
    for i in range(len(perm)):
        if i > 0 and i < len(perm) - 1:
            if perm[i] >= max(perm[:i]) and perm[i] <= min(perm[i + 1:]):
                flag = False
        elif i == 0:
            if perm[i] <= min(perm[i + 1:]):
                flag = False
        elif i == len(perm) - 1:
            if perm[i] >= max(perm[:i]):
                flag = False
    return flag


n = int(input())
l = map(int, input().split())

count = 0
s = set()
g = set()
permIter = permutations(l)
for perm in permIter:
    if perm in s:
        continue
    if check(perm):
        g.add(perm)
        count += 1
    s.add(perm)


print(count)
g = list(g)
g.sort()
with open('./temp.txt', 'w') as f:
    print(*g, sep='\n', file=f)
