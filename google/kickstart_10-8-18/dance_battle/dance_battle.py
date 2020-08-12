# Read file output list
def read_file(file):
    with open(file, "r") as f:
        lst = f.read().split("\n")
    return lst


# Parse info from list
def parse_info(lst):
    energy = int(lst.pop(0).split()[0])
    teams = lst.pop(0).split()
    for i in range(len(teams)):
        teams[i] = int(teams[i])
    return energy, teams


# Read input file
text = input("Input file: ")
read_list = read_file(text)
# Get amount of cases
case = int(read_list.pop(0))
# Create empty file
with open(text + ".out", "w") as f:
    print("", file=f, end="")
# Loop amount of cases
for i in range(case):
    # Get team info from data
    info = parse_info(read_list)
    energy = info[0]
    teams = sorted(info[1])
    # Init honor
    honor = 0
    # Honor calculator
    for j in range(len(teams)):
        # Battle if higher energy
        if energy > teams[0]:
            energy -= teams.pop(0)
            honor += 1
        else:
            # Quit if no honor or no more teams
            if len(teams) == 1 or honor == 0:
                break
            else:
                # Get more energy
                energy += teams.pop()
                honor -= 1
    # Output to file
    with open(text + ".out", "a") as f:
        print("Case #{}: {}".format(i+1, honor), file=f)
