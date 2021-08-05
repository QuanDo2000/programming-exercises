from itertools import chain, combinations

n = int(input())
a = list(map(int, input().split()))

subsets = list(chain.from_iterable(combinations(a, r)
                                   for r in range(1, n + 1)))

res = 0
for subset in subsets:
    temp = 0
    for ele in subset:
        temp = temp | ele
    res += temp
print(res)
