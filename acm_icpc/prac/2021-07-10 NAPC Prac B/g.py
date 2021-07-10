import sys

i = sys.stdin.readlines()

d = {}

for line in i:
    mess = line.split()
    if len(mess) == 0:
        continue
    if len(mess) > 1:
        d[mess[1]] = mess[0]
    else:
        if mess[0] not in d:
            print('eh')
        else:
            print(d[mess[0]])
