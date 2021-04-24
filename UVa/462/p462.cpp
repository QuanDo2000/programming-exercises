#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

unordered_map<char, int> ranks({{'A', 0}, {'2', 1}, {'3', 2}, {'4', 3}, {'5', 4}, {'6', 5}, {'7', 6}, {'8', 7}, {'9', 8}, {'T', 9}, {'J', 10}, {'Q', 11}, {'K', 12}});
unordered_map<char, int> suits({{'S', 0}, {'H', 1}, {'D', 2}, {'C', 3}});

const bool DEBUG = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string line, card;
    istringstream iss;
    int deck[15][5] = {};
    int idx, idy, points, ans, mx;

    while (getline(cin, line))
    {

        fill(&deck[0][0], &deck[0][0] + 15 * 5, 0);
        iss.clear();
        iss.str(line);

        if (DEBUG)
        {
            cout << line << "\n";
        }

        while (iss >> card)
        {
            if (DEBUG)
            {
                cout << card << " ";
            }
            idx = ranks[card.at(0)];
            idy = suits[card.at(1)];
            deck[idx][idy]++;
            deck[13][idy]++;
            deck[idx][4]++;
            deck[13][4]++;
        }

        ans = -1;
        mx = 0;

        // Rule 1
        points = deck[0][4] * 4 + deck[12][4] * 3 + deck[11][4] * 2 + deck[10][4];
        for (int i = 0; i < 4; i++)
        {
            // Check rules 2-4
            if (deck[12][i] >= 1 && deck[13][i] == deck[12][i])
            {
                points--;
            }
            if (deck[11][i] >= 1 && deck[13][i] - deck[11][i] <= 1)
            {
                points--;
            }
            if (deck[10][i] >= 1 && deck[13][i] - deck[10][i] <= 2)
            {
                points--;
            }
            // Check for stopped
            if (deck[0][i] > 0 || (deck[12][i] > 0 && deck[13][i] > 1) || (deck[11][i] > 0 && deck[13][i] > 2))
            {
                deck[14][i] = 1;
                deck[14][4]++;
            }
        }

        if (DEBUG)
        {
            cout << "\n"
                 << points << "\n";
            for (int i = 0; i < 15; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    cout << deck[i][j] << " ";
                }
                cout << "\n";
            }
        }

        // NO-TRUMP
        if (points >= 16 && deck[14][4] == 4)
        {
            ans = 5;
        }

        if (ans == -1)
        {
            // Check rules 5-7
            for (int i = 0; i < 4; i++)
            {
                // Check rules 2-4
                if (deck[13][i] == 2)
                {
                    points++;
                }
                else if (deck[13][i] == 1)
                {
                    points += 2;
                }
                else if (deck[13][i] == 0)
                {
                    points += 2;
                }
                // Get max number of cards in each suit
                if (deck[13][mx] < deck[13][i])
                {
                    mx = i;
                }
            }
            if (points < 14)
            {
                ans = 0;
            }
            else
            {
                ans = 1 + mx;
            }
        }

        switch (ans)
        {
        case 0:
            cout << "PASS";
            break;
        case 1:
            cout << "BID S";
            break;
        case 2:
            cout << "BID H";
            break;
        case 3:
            cout << "BID D";
            break;
        case 4:
            cout << "BID C";
            break;
        case 5:
            cout << "BID NO-TRUMP";
            break;

        default:
            break;
        }
        cout << "\n";
    }

    return 0;
}