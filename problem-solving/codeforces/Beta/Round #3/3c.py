def check(b):
    return b[0] == b[1] and b[1] == b[2] or \
        b[3] == b[4] and b[4] == b[5] or \
        b[6] == b[7] and b[7] == b[8] or \
        b[0] == b[3] and b[3] == b[6] or \
        b[1] == b[4] and b[4] == b[7] or \
        b[2] == b[5] and b[5] == b[8] or \
        b[0] == b[4] and b[4] == b[8] or \
        b[2] == b[4] and b[4] == b[6]


b = []

for _ in range(3):
    b += list(input())
print(b)
x = 0
o = 0
for line in b:
    for elem in line:
        if elem == 'X':
            x += 1
        elif elem == '0':
            o += 1
if x - o > 1 or o > x:
    print('illegal')
elif x == o:
    if check(b):
        print('1 won')
    else:
        print('first')
elif x - 1 == o and x != 5:
    if check(b):
        print('2 won')
    else:
        print('second')
elif x - 1 == o and x == 5:
    if check(b):
        print('3 won')
    else:
        print('draw')
