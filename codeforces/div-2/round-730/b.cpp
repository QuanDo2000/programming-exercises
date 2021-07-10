#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int t, n;
ll a, sum, mod, ans;

void solve()
{
    sum = 0;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        sum += a;
    }
    mod = sum % n;
    ans = mod * (n - mod);
    cout << ans << "\n";
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