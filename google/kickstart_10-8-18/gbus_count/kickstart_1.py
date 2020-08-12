def gbus_count(file):
    # Read file
    with open(file) as f:
        read_data = f.read()
    read_list = read_data.split("\n")

    # Get amount of cases
    case = int(read_list.pop(0))
    # Create new file
    with open(file + ".output", "w") as f:
        print(file=f, end="")
    for i in range(case):
        n = int(read_list.pop(0))
        a = []
        b = []
        c = []
        cities = read_list.pop(0).split()
        for j in range(n):
            a.append(int(cities[j*2]))
            b.append(int(cities[j*2+1]))
        p = int(read_list.pop(0))
        for j in range(p):
            c.append(int(read_list.pop(0)))
        output = []
        for j in range(len(c)):
            y = 0
            for k in range(len(a)):
                if c[j] >= a[k] and c[j] <= b[k]:
                    y += 1
            output.append(y)
        # Print output to file
        with open(file + ".output", "a") as f:
            print("Case #{0}: ".format(i+1), end="", file=f)
            for j in range(len(output)):
                print(output[j], end=" ", file=f)
            print(file=f)
        if read_list != []:
            read_list.pop(0)


# Read file and write output
file = input("Enter file name: ")
gbus_count(file)
