s = input()

n = len(s)
d = [0] * 26

for letter in s:
    d[ord(letter) - ord('a')] += 1

if d.count(0) >= 24:
    print(0)
else:
    print(n - sum(sorted(d)[-2:]))
