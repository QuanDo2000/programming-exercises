ri, rj = map(int, input().split())
si = 'D'
sj = 'E'

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
        if n_cousin % 10 not in [1, 2, 3]:
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
    if (ri - 1) % 10 not in [1, 2, 3]:
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
