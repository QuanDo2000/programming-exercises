s = input()
a = s.count('a')
if a > (len(s) / 2):
    print(len(s))
else:
    print(a*2-1)
