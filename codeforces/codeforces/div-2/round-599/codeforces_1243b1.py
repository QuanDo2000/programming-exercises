for _ in range(int(input())):
    n = int(input())
    s = input()
    t = input()
    diff = []
    for a, b in zip(s, t):
        if a != b:
            diff.append((a, b))
    if len(diff) != 2:
        print('No')
    else:
        if diff[0] != diff[1]:
            print('No')
        else:
            print('Yes')
