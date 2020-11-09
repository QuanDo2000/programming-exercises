n = int(input())
hate = 'I hate'
love = 'I love'
res = []
for i in range(n):
    if i > 0:
        res.append('that')
    if i % 2 == 0:
        res.append(hate)
    else:
        res.append(love)
res.append('it')
print(' '.join(res))
