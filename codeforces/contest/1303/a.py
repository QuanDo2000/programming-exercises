t = int(input())
for _ in range(t):
    s = input()
    zeros = s.count('0')
    if zeros == len(s):
        print(0)
    else:
        a = s.index('1')
        b = s[::-1].index('1')
        print(zeros - a - b)
