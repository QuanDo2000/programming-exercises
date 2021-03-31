from operator import itemgetter

n = int(input())

names = []
for _ in range(n):
    names.append(list(input().split()))

names = sorted(names, key=itemgetter(1, 0))

for name in names:
    print(' '.join(name))
