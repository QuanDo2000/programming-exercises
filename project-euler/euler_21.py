"""
ID: 21
Name: Amicable numbers
Description:
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
Link: https://projecteuler.net/problem=21
"""


def find_divisors(num):
    """Return a list of all proper divisors for input number."""
    ret_list = []
    for idx in range(1, (num // 2) + 1):
        if num % idx == 0:
            ret_list.append(idx)
    return ret_list


sum_map = {}
for idx in range(1, 10000):
    sum_map[idx] = sum(find_divisors(idx))

amicable_nums = set()
for idx in range(1, 10000):
    if sum_map[idx] in sum_map and sum_map[sum_map[idx]] == idx and idx != sum_map[idx]:
        amicable_nums.add(idx)
        amicable_nums.add(sum_map[idx])

ans = sum(amicable_nums)
print('The sum of amicable numbers is {}'.format(ans))
