t = int(input())
chars = ['a', 'b', 'c']


def main():
    s = list(input())
    l = len(s)
    for i in range(l-1):
        if s[i] == s[i+1] and s[i] != '?':
            print(-1)
            return
    if l == 1:
        if s[0] == '?':
            s[0] = 'a'
    for i in range(l):
        if s[i] == '?':
            for char in chars:
                if i == 0:
                    if char != s[i+1]:
                        s[i] = char
                elif i == (l - 1):
                    if char != s[i-1]:
                        s[i] = char
                else:
                    if char != s[i-1] and char != s[i+1]:
                        s[i] = char
    for i in range(l):
        if s[i] == '?':
            print(-1)
            return
    ans = ''.join(s)
    print(ans)


for _ in range(t):
    main()
