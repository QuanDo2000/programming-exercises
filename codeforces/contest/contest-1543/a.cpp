#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int t;
ll a, b, dif, mod;

void solve()
{
    cin >> a >> b;
    if (a == b)
    {
        cout << "0 0\n";
        return;
    }
    dif = abs(a - b);
    mod = a % dif;
    if (mod * 2 > dif)
    {
        mod = dif - mod;
    }
    cout << dif << " " << mod << "\n";
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