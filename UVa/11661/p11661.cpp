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

    int l, ans, dif;
    char prev;
    string line;

    while (cin >> l)
    {
        if (l == 0)
        {
            return 0;
        }
        cin >> line;

        ans = l;
        dif = 0;
        prev = '.';

        for (char &ch : line)
        {
            dif++;
            if (ch == 'Z')
            {
                ans = 0;
            }
            else if (prev == '.' && ch != prev)
            {
                prev = ch;
                dif = 0;
            }
            else if (ch != prev && prev != '.' && ch != '.')
            {
                prev = ch;
                if (dif < ans)
                {
                    ans = dif;
                }
                dif = 0;
            }
            else if (ch == prev && prev != '.')
            {
                dif = 0;
            }
        }
        cout << ans << "\n";
    }

    return 0;
}