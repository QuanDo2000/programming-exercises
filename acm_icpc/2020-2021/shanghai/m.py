from collections import defaultdict


DEBUG = False

ignore = defaultdict(int)
tree = {}


def dfs1(x):
    global tree, ignore
    if len(tree[x][1]) == 0:
        return
    num = 0
    count = 0
    for child in tree[x][1]:
        dfs1(child)
        if ignore[child] == 1:
            count += 1
        num += tree[child][0]
    if count == len(tree[x][1]) and x != "/":
        num = 1
        ignore[x] = 1
    tree[x][0] = num


def solve():
    global tree, ignore
    tree = {"/": [0, []]}
    n, m = map(int, input().split())
    ignore = defaultdict(int)
    for _ in range(n):
        path = list(input().split('/'))
        prev = "/"
        par = "/"
        for i, file in enumerate(path):
            fname = "{}_{}_{}".format(par, file, i)
            if fname not in tree[prev][1]:
                tree[prev][1].append(fname)
            if fname not in tree:
                tree[fname] = [0, []]
            if file == path[-1]:
                tree[fname][0] = 1
                ignore[fname] = 1
            prev = fname
            par = file
    for _ in range(m):
        path = list(input().split('/'))
        prev = "/"
        par = "/"
        for i, file in enumerate(path):
            fname = "{}_{}_{}".format(par, file, i)
            if fname not in tree[prev][1]:
                tree[prev][1].append(fname)
            if fname not in tree:
                tree[fname] = [0, []]
            prev = fname
            par = file

    dfs1("/")
    print(tree["/"][0])

    if DEBUG:
        print(tree, ignore, sep="\n")


t = int(input())
for _ in range(t):
    solve()
