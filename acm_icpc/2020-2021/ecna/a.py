def lca(tree, ri, rj, si, sj):
    # Find closest common ancestor
    ti, tj = ri, rj
    pi, pj = si, sj
    while ti < tj:
        pj = tree[pj][2]
        tj = tree[pj][0]
    while tj < ti:
        pi = tree[pi][2]
        ti = tree[pi][0]
    while pi != pj:
        pi = tree[pi][2]
        pj = tree[pj][2]
        ti = tree[pi][0]
        tj = tree[pj][0]

    ri = ri - ti
    rj = rj - tj
    return ri, rj


t, p = map(int, input().split())


tree = {}
for _ in range(t):
    line = input().split()
    parent = line[0]
    children = line[2:]
    if parent not in tree:
        parent_row = 0
        tree[parent] = [parent_row, children[:], '']
    else:
        parent_row = tree[parent][0]
        tree[parent][1] = children[:]

    while children:
        child = children.pop(0)
        if child in tree:
            if tree[child][2] == '':
                tree[child][2] = parent
            tree[child][0] = tree[tree[child][2]][0] + 1
            for c in tree[child][1]:
                children.append(c)
        else:
            tree[child] = [parent_row + 1, [], parent]

# print(tree)

for _ in range(p):
    si, sj = input().split()
    ri, rj = tree[si][0], tree[sj][0]
    # print(ri, tree[si][2], rj, tree[sj][2])

    # Find closest common ancestor
    ri, rj = lca(tree, ri, rj, si, sj)

    swap = False
    if ri > rj:
        ri, rj = rj, ri
        si, sj = sj, si
        swap = True

    # print(ri, pi, rj, pj)

    if (ri == 0 or rj == 0) and ri != rj:
        diff = abs(ri - rj)
        if diff == 1:
            print('{} is the child of {}'.format(sj, si))
        elif diff > 1:
            num_great = diff - 2
            if num_great == 0:
                print('{} is the grandchild of {}'.format(sj, si))
            else:
                str_great = ' '.join(['great'] * num_great)
                print('{} is the {} grandchild of {}'.format(
                    sj, str_great, si))
    elif ri == rj:
        if ri == 1:
            print('{} and {} are siblings'.format(si, sj))
        else:
            n_cousin = ri - 1
            if n_cousin % 10 not in [1, 2, 3] or n_cousin in [11, 12, 13]:
                print('{} and {} are {}th cousins'.format(si, sj, n_cousin))
            elif n_cousin % 10 == 1:
                print('{} and {} are {}st cousins'.format(si, sj, n_cousin))
            elif n_cousin % 10 == 2:
                print('{} and {} are {}nd cousins'.format(si, sj, n_cousin))
            elif n_cousin % 10 == 3:
                print('{} and {} are {}rd cousins'.format(si, sj, n_cousin))

    elif ri < rj:
        if swap:
            si, sj = sj, si
        if (ri - 1) % 10 not in [1, 2, 3] or ri in [11, 12, 13]:
            th_str = '{}th'.format(ri - 1)
        elif (ri - 1) % 10 == 1:
            th_str = '{}st'.format(ri - 1)
        elif (ri - 1) % 10 == 2:
            th_str = '{}nd'.format(ri - 1)
        elif (ri - 1) % 10 == 3:
            th_str = '{}rd'.format(ri - 1)
        if (rj - ri) == 1:
            time_str = 'time'
        else:
            time_str = 'times'

        print('{} and {} are {} cousins, {} {} removed'.format(
            si, sj, th_str, rj - ri, time_str))
