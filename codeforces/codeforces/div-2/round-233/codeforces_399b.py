n = int(input())
s = list(input())
count = 0
ans = [1]
for i in range(50):
    ans.append(sum(ans) + 1)
# print(ans)
for i in range(n):
    char = s[i]
    if char == 'B':
        count += ans[i]
print(count)
# while 'B' in s:
#     if s[0] == 'B':
#         count += 1
#         s[0] = 'R'
#     else:
#         x = s.index('B')
#         for i in range(x):
#             s[i] = 'B'
#         s[x] = 'R'
#         count += 1
#     print(''.join(s))
