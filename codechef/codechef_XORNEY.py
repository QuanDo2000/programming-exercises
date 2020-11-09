"""
CodeChef Problem: XORNEY
https://www.codechef.com/problems/XORNEY
"""

# Support function to output 1 of 4 values in list
# If a % 4 == 0 => XOR(a) = a
#             1 =>          1
#             2 =>          a+1
#             3 =>          0


def f(a):
    res = [a, 1, a + 1, 0]
    return res[a % 4]


# Get XOR(^) for range
# XOR(a -> b) = XOR(0 -> a) ^ XOR(0 -> b)
def getXor(a, b):
    return f(b) ^ f(a - 1)


# Get input of lines
for i in range(int(input())):
    # Read range from lines
    l, r = map(int, input().split())
    # Calculate and print result
    result = getXor(l, r)
    if result % 2 == 0:
        print("Even")
    else:
        print("Odd")
