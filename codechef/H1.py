"""
CodeChef Problem: H1
https://www.codechef.com/problems/H1
"""
# List of primes possible
prime = [3, 5, 7, 11, 13, 17]
# List of swaps that can be made
swaps = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 5), (3, 6), (3, 4),
         (4, 5), (4, 7), (5, 8), (6, 7), (7, 8)]

current = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
visited = {(1, 2, 3, 4, 5, 6, 7, 8, 9): 0}

# Generate all possibilities
while len(current) != 0:
    # Remove board config from current
    state = current.pop(0)
    # Check all possible swap moves
    for move in swaps:
        # If sum is in prime
        if state[move[0]] + state[move[1]] in prime:
            # Copy current state
            s2 = state[:]
            # Swap values
            s2[move[0]], s2[move[1]] = state[move[1]], state[move[0]]
            # If not in visited
            if tuple(s2) not in visited:
                # Add config to visited with corresponding moves value
                visited[tuple(s2)] = visited[tuple(state)] + 1
                # Add config to current for further consideration
                current.append(s2)

# Loop test cases
for _ in range(int(input())):
    input()
    # Get grid from input
    grid = []
    grid += list(map(int, input().split()))
    grid += list(map(int, input().split()))
    grid += list(map(int, input().split()))
    # Print amount of moves associated with grid config
    if tuple(grid) in visited:
        print(visited[tuple(grid)])
    else:
        print(-1)
