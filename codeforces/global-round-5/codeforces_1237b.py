n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = [-1] * n
c = [-1] * n
count = 0
# for i in range(n):
#     cari = b.index(a[i])
#     for j in range(i+1, n):
#         if b.index(a[j]) < cari:
#             if a[j] not in o:
#                 o.append(a[j])
#                 count += 1

# for i in range(n):
#     cari = b.index(a[i])
#     for car in b[:cari]:
#         if car not in a[:i]:
#             if car not in o:
#                 o.append(car)
#                 count += 1

# i = 0
# for car in b:
#     if car != a[i]:
#         a.remove(car)
#         count += 1
#     else:
#         i += 1

for i in range(n):
    pos[b[i] - 1] = i
for i in range(n):
    c[i] = pos[a[i] - 1]
mx = -1
for i in range(n):
    if (c[i] > mx):
        mx = c[i]
    else:
        count += 1

print(count)
