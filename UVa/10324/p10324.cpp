#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const int MAX_N = 1e6 + 1;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    char prev;
    string line;
    int i, n, a, b, t = 1;
    vector<int> change;

    while (cin >> line)
    {
        change.clear();
        change.push_back(0);
        prev = ' ';
        i = 0;
        for (auto &ch : line)
        {
            if (prev != ' ')
            {
                if (prev != ch)
                {
                    change.push_back(change.at(i - 1) + 1);
                }
                else
                {
                    change.push_back(change.at(i - 1));
                }
            }
            prev = ch;
            i++;
        }

        cin >> n;
        cout << "Case " << t++ << ":\n";
        for (i = 0; i < n; i++)
        {
            cin >> a >> b;
            if (change.at(a) == change.at(b))
            {
                cout << "Yes";
            }
            else
            {
                cout << "No";
            }
            cout << "\n";
        }
    }

    return 0;
}