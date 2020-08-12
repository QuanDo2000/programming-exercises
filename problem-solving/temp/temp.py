from random import randint


def quicksort(a):
    if len(a) <= 1:
        return a
    key = randint(0, len(a) - 1)
    l = []
    r = []
    for i in range(len(a)):
        if i == key:
            continue
        if a[i] < a[key]:
            l.append(a[i])
        else:
            r.append(a[i])
    # print(l, r)
    l = quicksort(l)
    r = quicksort(r)
    return l + [a[key]] + r


def mergesort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    l = mergesort(a[:mid])
    r = mergesort(a[mid:])
    i = 0
    j = 0
    b = []
    while (i < len(l) and j < len(r)):
        if l[i] < r[j]:
            b.append(l[i])
            i += 1
        else:
            b.append(r[j])
            j += 1
    if i < len(l):
        b += l[i:]
    if j < len(r):
        b += r[j:]
    # print(b)
    return b


n = int(input())
a = [randint(1, n) for _ in range(n)]
print(a)
a = quicksort(a)
print(a)
