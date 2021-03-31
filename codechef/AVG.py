"""
CodeChef Problem: AVG
https://www.codechef.com/problems/AVG
"""

# Loop test cases
for _ in range(int(input())):
    # Input
    # n for number of elements remaining
    # k for number of elements removed
    # v for average of all elements
    # a is list of all known elements (length of n)
    n, k, v = map(int, input().split())
    a = list(map(int, input().split()))

    # Calculate the value of the remove element
    # num = (average * total_elements - sum_of_remaining) / elements_removed
    s = 0
    for num in a:
        s += num
    num = (v * (n + k) - s) / k
    # Result must be integer and larger than 0
    if num > int(num) or (num <= 0):
        print(-1)
    else:
        print(int(num))
