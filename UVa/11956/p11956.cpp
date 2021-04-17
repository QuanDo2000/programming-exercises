#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int tc, t = 1, p;
    vector<int> dump(100);
    string line;

    cout << setfill('0') << uppercase;

    cin >> tc;
    cin.ignore();
    while (tc--)
    {
        fill(dump.begin(), dump.end(), 0);
        getline(cin, line);
        p = 0;
        for (char &ch : line)
        {
            if (ch == '+')
            {
                if (dump.at(p) == 255)
                {
                    dump.at(p) = 0;
                }
                else
                {
                    dump.at(p)++;
                }
            }
            else if (ch == '-')
            {
                if (dump.at(p) == 0)
                {
                    dump.at(p) = 255;
                }
                else
                {
                    dump.at(p)--;
                }
            }
            else if (ch == '>')
            {
                if (p == 99)
                {
                    p = 0;
                }
                else
                {
                    p++;
                }
            }
            else if (ch == '<')
            {
                if (p == 0)
                {
                    p = 99;
                }
                else
                {
                    p--;
                }
            }
        }
        cout << dec;
        cout << "Case " << t++ << ":";
        cout << hex;
        for (auto &num : dump)
        {
            cout << " " << setw(2) << num;
        }
        cout << "\n";
    }

    return 0;
}