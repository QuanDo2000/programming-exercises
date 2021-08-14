import sys
import math


def isprime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


inp = sys.stdin.readlines()
inp = list(map(str.split, inp))

nums = []

for i, line in enumerate(inp):
    if type(line) != list:
        nums.append(line.strip())
    else:
        for substr in line:
            nums.append(substr.strip())

if len(nums) != 3:
    print(0)
else:
    flag = True
    for num in nums:
        if num[0] == '0':
            flag = False
            break
        for char in num:
            if not char.isdigit():
                flag = False
                break
        if not flag:
            break
    if not flag:
        print(0)
    else:
        nums = list(map(int, nums))
        # print(1)
        if nums[0] <= 3 or nums[0] > 1e9 or nums[0] % 2 != 0:
            print(0)
        elif (not isprime(nums[1])) or (not isprime(nums[2])):
            print(0)
        elif nums[1] + nums[2] == nums[0]:
            print(1)
        else:
            print(0)
