#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void solve()
{
    int xa, ya, xb, yb, xf, yf;
    cin >> xa >> ya;
    cin >> xb >> yb;
    cin >> xf >> yf;

    int ans = 0;
    ans = abs(xa - xb) + abs(ya - yb);
    if (xa == xb && xa == xf)
    {
        if ((yf < ya && yf > yb) || (yf < yb && yf > ya))
        {
            ans += 2;
        }
    }
    else if (ya == yb && ya == yf)
    {
        if ((xf < xa && xf > xb) || (xf < xb && xf > xa))
        {
            ans += 2;
        }
    }
    cout << ans << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }

    return 0;
}