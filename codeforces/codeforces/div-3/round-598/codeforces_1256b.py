for _ in range(int(input())):
    q = int(input())
    n = list(map(int, input().split()))
    pos = 0
    while (pos < q):
        nxt = n.index(min(n[pos:]))
        el = n.pop(nxt)
        n.insert(pos, el)
        if (pos == nxt):
            pos = nxt + 1
        else:
            pos = nxt
    print(' '.join([str(i) for i in n]))
