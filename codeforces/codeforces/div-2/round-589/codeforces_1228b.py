h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
# table = []
# for i in range(h):
#     table.append([-1] * w)
# for i in range(h):
#     if r[i] == 0:
#         table[i][0] = 0
#     else:
#         for j in range(r[i]):
#             table[i][j] = 1
#         if j < w-1:
#             table[i][j+1] = 0
# for i in range(w):
#     if c[i] == 0:
#         if table[0][i] == 1:
#             print(0)
#             exit()
#         else:
#             table[0][i] = 0
#             continue
#     else:
#         for j in range(c[i]):
#             if table[j][i] == 0:
#                 print(0)
#                 exit()
#             else:
#                 table[j][i] = 1
#                 continue
#         if j < h-1:
#             table[j+1][i] = 0
# res = 1
# for row in table:
#     count = row.count(-1)
#     if count != 0:
#         res *= 2 ** count
# print(res % (10 ** 9 + 7))


count = 0
for i in range(h):
    for j in range(w):
        if (j == r[i] and c[j] > i) or (i == c[j] and r[i] > j):
            print(0)
            exit()
        if j > r[i] and i > c[j]:
            count += 1
res = 2 ** count
print(res % (10 ** 9 + 7))
