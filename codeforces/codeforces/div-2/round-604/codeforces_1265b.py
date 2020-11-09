# def check(p, m):
#     i1 = p.index(1)
#     # im = p.index(m)
#     # l = min(i1, im)
#     # r = max(i1, im)
#     # # print(m, i1, im, l, r)
#     # for num in p[l:r+1]:
#     #     if num > m:
#     #         return False
#     # while (l > 0 and p[l-1] < m) or (r < len(p)-1 and p[r+1] < m):
#     #     # print(l, r)
#     #     if l > 0 and p[l-1] < m:
#     #         l -= 1
#     #     if r < len(p)-1 and p[r+1] < m:
#     #         r += 1
#     # # print('\t', l, r)
#     # if len(p[l:r+1]) == m:
#     #     return True
#     # else:
#     #     return False
#     for i in range(max(i1-m+1, 0), min(i1+1, len(p)-m+1)):
#         # print(p[i:i+m])
#         if max(p[i:i+m]) == m:
#             return True
#     else:
#         return False


def main():
    n = int(input())
    p = list(map(int, input().split()))
    index = [0] * n
    ans = [0] * n
    for i in range(n):
        index[p[i]-1] = i
    l, r = [0] * n, [0] * n
    l[0], r[0] = index[0], index[0]
    for i in range(1, n):
        l[i] = min(l[i-1], index[i])
        r[i] = max(r[i-1], index[i])
    # print(index, l, r, sep='\n')
    for i in range(n):
        if r[i] - l[i] == i:
            ans[i] = 1
    print(''.join([str(x) for x in ans]))


t = int(input())
for _ in range(t):
    main()
