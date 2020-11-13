"""
ID: 22
Name: Names scores
Description:
    Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
Link: https://projecteuler.net/problem=22
"""


def read_file(filename):
    """Return the parsed data from input file."""
    with open('./data/{}.txt'.format(filename), 'r') as f:
        raw_data = f.readlines()
    names_list = raw_data[0].split(',')
    names_list = [name.replace('"', '') for name in names_list]
    names_list = sorted(names_list)
    return names_list


def get_alpha_score(in_str):
    """Return the sum of alphabetical values of the input string."""
    ret_score = 0
    for char in in_str:
        ret_score += ord(char) - ord('A') + 1
    return ret_score


names = read_file('p022_names')
total_scores = 0
for idx, name in enumerate(names):
    score = get_alpha_score(name)
    if name == 'COLIN':
        print(score * (idx + 1))
    total_scores += score * (idx + 1)

print('The total names scores is {}'.format(total_scores))
