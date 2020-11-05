"""
CodeChef Problem: DEPCHEF
https://www.codechef.com/problems/DEPCHEF
"""
# Loop test cases
for _ in range(int(input())):
    # Get test case
    # a is list of attack values for every soldier
    # d is list of defense values for every soldier
    n = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))

    # Acceptable values
    r = []
    # Check for acceptable values and store into list
    # Value is acceptable if defense value of middle solder
    # is larger than sum of attack value of surrounding soldier
    for i in range(len(d)):
        # Check last index
        if i == (len(d) - 1):
            if d[i] > (a[i - 1] + a[0]):
                r.append(d[i])
        else:
            if d[i] > (a[i - 1] + a[i + 1]):
                r.append(d[i])
    # Get the max value in list of acceptable values or print -1 if list empty
    if len(r) == 0:
        print(-1)
    else:
        print(max(r))
