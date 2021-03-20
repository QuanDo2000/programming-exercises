import sys
from collections import defaultdict


DEBUG = False

order = [(":-P", "P"),
         (":D", "D"),
         (":C", "C"),
         ("8-0", "8"),
         (":-E", "E"),
         ("%0", "%"),
         (":-X", "X"),
         (":-0", "0"),
         (":~(", "~"),
         (":-\\", "\\"),
         ("[:|||:]", "["),
         (":-|", "|")]


sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
s = sys.stdin.readline()


d = defaultdict(int)
for c in s:
    if DEBUG:
        print(c)
    d[c] += 1

if DEBUG:
    print(s)
    print(d)

for ss, uniq in order:
    if DEBUG:
        print(uniq, d[uniq])
    while d[uniq] > 0:
        d[uniq] -= 1
        for char in ss:
            if char != uniq:
                d[char] -= 1
        print(ss)

while d['-'] > 0:
    d['-'] -= 1
    d[';'] -= 1
    if d[')'] > 0:
        d[')'] -= 1
        print(';-)')
    elif d['('] > 0:
        d['('] -= 1
        print(';-(')

while d[':'] > 0:
    d[':'] -= 1
    if d[')'] > 0:
        d[')'] -= 1
        print(':)')
    elif d['('] > 0:
        d['('] -= 1
        print(':(')
print('LOL')

if DEBUG:
    print(d)
