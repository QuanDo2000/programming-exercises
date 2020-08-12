# CodeChef Problem: WTCH
# https://www.codechef.com/problems/WTCH

import math  # ceil()

# Loop test cases
for i in range(int(input())):
    # Read input
    n = input()
    # Split at "1"
    s = input().split("1")
    num = 0
    # Special case for only 0
    # All towers are empty
    if len(s) == 1:
        print(math.ceil(len(s[0]) / 2))
        continue
    for j in range(len(s)):
        # Only consider towers which is not directly adjacent
        if j == 0 or j == (len(s) - 1):
            # Special case for 1st and last position
            # Since only has 1 side to calculate from
            if len(s[j]) > 1:
                num += math.ceil((len(s[j]) - 1) / 2)
        else:
            if len(s[j]) > 2:
                num += math.ceil((len(s[j]) - 2) / 2)
    print(num)
