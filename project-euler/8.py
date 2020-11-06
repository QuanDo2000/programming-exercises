"""
ID: 8
Name: Largest product in a series
Description:
    The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
Link: https://projecteuler.net/problem=8
"""


import sys
import inspect
import os


def product_series(text, k=13):
    """Return product of k amount of integer in a series of number."""
    product = 1
    for num in text[:k]:
        product *= int(num)
    return product


def read_file(filename="008_series.txt"):
    """Read file for series and split series at 0."""
    # Get current file path
    path = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe()))) + "/resource/" + filename
    with open(path, "r") as f:
        series = ""
        for line in f:
            series += line
    series = series.replace("\n", "")
    series = series.split("0")
    return series


def max_product_series(series, k=13):
    """Return the maximum product in a series."""
    max_product = 1
    for serie in series:
        if len(serie) >= k:
            for i in range(k, len(serie) + 1):
                if product_series(serie[i - k:i]) > max_product:
                    max_product = product_series(serie[i - k:i])
    return max_product


# Input
name = '008_series.txt'
try:
    series = read_file(name)
    k = int(input("Enter amount of numbers: "))
except FileNotFoundError:
    # Handle file not found error
    print("File Not Found.\nExit...")
    sys.exit()
except ValueError:
    # Handle input error
    print("Invalid Input.\nExit...")
    sys.exit()

# Print result
print("\nThe series is:")
for serie in series:
    print(serie, end="")
res = max_product_series(series, k)
print("\nThe maximum product with {} numbers is: {:,}".format(k, res))
