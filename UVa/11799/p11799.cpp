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

    int tc, n, c, mx, t = 1;

    cin >> tc;
    while (tc--)
    {
        mx = 0;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> c;
            if (c > mx)
            {
                mx = c;
            }
        }
        cout << "Case " << t++ << ": " << mx << "\n";
    }

    return 0;
}