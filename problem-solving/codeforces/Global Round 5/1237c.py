n = int(input())
p = [list(map(int, input().split())) + [i]
     for i in range(n)] + [[10**9, 10**9, 10**9]]
p.sort(key=lambda x: tuple(x[:-1]))

rem = []

i = 0
while i < n:
    if p[i][:2] == p[i+1][:2]:
        print(p[i][-1]+1, p[i+1][-1]+1)
        i += 2
    else:
        rem.append(p[i])
        i += 1

rem += [p[n]]
rem2 = []

n = len(rem)
i = 0
while i < n - 1:
    if rem[i][0] == rem[i+1][0]:
        print(rem[i][-1]+1, rem[i+1][-1]+1)
        i += 2
    else:
        rem2.append(rem[i])
        i += 1

for i in range(0, len(rem2), 2):
    print(rem2[i][-1]+1, rem2[i+1][-1]+1)

# s = [p.pop(0)]
# while p:
#     # print()
#     # for i in s:
#     #     print(i)
#     new = p.pop(0)
#     if not s:
#         s.append(new)
#         continue
#     if new[:-2] == s[-1][:-2]:
#         print('{} {}'.format(new[-1]+1, s.pop()[-1] + 1))
#         continue
#     s.append(new)

# p = s
# s = [p.pop(0)]
# while p:
#     # print()
#     # for i in s:
#     #     print(i)
#     new = p.pop(0)
#     if not s:
#         s.append(new)
#         continue
#     if new[:-3] == s[-1][:-3]:
#         print('{} {}'.format(new[-1]+1, s.pop()[-1] + 1))
#         continue
#     s.append(new)
# # print(s)
