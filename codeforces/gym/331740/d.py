t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    ans = 'Yes' if a & b else 'No'
    print(ans)
