# CodeChef Problem: FANCY
# https://www.codechef.com/problems/FANCY

# Loop test cases
for _ in range(int(input())):
    # Input a list containing every word.
    s = input().split()
    # Check if the word 'not' is in the list
    if "not" in s:
        print("Real Fancy")
    else:
        print("regularly fancy")
