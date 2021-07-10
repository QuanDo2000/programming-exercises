#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int t, n, odds, even, temp;

void solve()
{
    cin >> n;
    odds = 0;
    even = 0;
    for (int i = 0; i < 2 * n; i++)
    {
        cin >> temp;
        if (temp % 2 == 0)
        {
            even++;
        }
        else
        {
            odds++;
        }
    }
    if (even == odds)
    {
        cout << "Yes\n";
    }
    else
    {
        cout << "No\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;
    while (t--)
    {
        solve();
    }

    return 0;
}