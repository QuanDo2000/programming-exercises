#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const bool DEBUG = 0;

const int MAX_N = 1e5 + 2;

void solve()
{
    int n;
    cin >> n;

    ll b, ans = 1;
    for (int i = 0; i < n; i++)
    {
        if (ans > (LLONG_MAX / 2))
        {
            ll temp = (ans - (LLONG_MAX / 2)) / MOD + 1;
            ans -= temp * MOD;
        }
        ans = (ans * 2);
        cin >> b;
        if (DEBUG)
        {
            cout << ans << " " << b << "\n";
        }
        if (b > ans)
        {
            cout << "error\n";
            return;
        }
        ans -= b;
    }
    cout << ans % MOD << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}