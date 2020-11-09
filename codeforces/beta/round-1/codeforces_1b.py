import re
import string


char = string.ascii_uppercase
for _ in range(int(input())):
    s = input()
    match0 = re.search('^R([0-9]+)C([0-9]+)$', s)
    match1 = re.search('^([A-Z]+)([0-9]+)$', s)
    if match0:
        temp = int(match0[2])
        row = ''
        while temp != 0:
            row += char[(temp - 1) % 26]
            if (temp % 26 == 0):
                temp -= 1
            temp //= 26
        row = row[::-1]
        print(row + match0[1])
    if match1:
        ans = 'R' + match1[2] + 'C'
        temp = list(match1[1])
        temp = temp[::-1]
        num = 0
        for i in range(len(temp)):
            temp[i] = char.find(temp[i]) + 1
            num += temp[i] * (26 ** i)
        print(ans + str(num))
