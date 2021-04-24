#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

unordered_map<char, int> ranks({{'A', 13}, {'2', 1}, {'3', 2}, {'4', 3}, {'5', 4}, {'6', 5}, {'7', 6}, {'8', 7}, {'9', 8}, {'T', 9}, {'J', 10}, {'Q', 11}, {'K', 12}});
unordered_map<char, int> suits({{'S', 2}, {'H', 3}, {'D', 1}, {'C', 0}});

struct cmp
{
    bool operator()(string a, string b) const
    {
        if (suits[a.at(0)] < suits[b.at(0)])
        {
            return true;
        }
        else if (suits[a.at(0)] == suits[b.at(0)])
        {
            if (ranks[a.at(1)] < ranks[b.at(1)])
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    set<string, cmp> ss[4];
    string line, card;
    char first;
    int p;

    while (cin >> first)
    {
        if (first == '#')
        {
            return 0;
        }
        cin.ignore();

        switch (first)
        {
        case 'S':
            p = 1;
            break;
        case 'W':
            p = 2;
            break;
        case 'N':
            p = 3;
            break;
        case 'E':
            p = 0;
            break;

        default:
            p = 0;
            break;
        }

        for (int i = 0; i < 4; i++)
        {
            ss[i].clear();
        }

        for (int i = 0; i < 2; i++)
        {
            getline(cin, line);
            for (int j = 0; j < 26; j++)
            {
                card = line.at(2 * j);
                card += line.at(2 * j + 1);
                ss[p].insert(card);
                p = (p + 1) % 4;
            }
        }

        for (int i = 0; i < 4; i++)
        {
            switch (i)
            {
            case 0:
                cout << "S:";
                break;
            case 1:
                cout << "W:";
                break;
            case 2:
                cout << "N:";
                break;
            case 3:
                cout << "E:";
                break;

            default:
                break;
            }
            for (auto &card : ss[i])
            {
                cout << " " << card;
            }
            cout << "\n";
        }
    }

    return 0;
}