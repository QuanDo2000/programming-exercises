#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const bool DEBUG = 0;

void solve()
{
    int m, a, b, c;
    cin >> m >> a >> b >> c;
    if ((a + b + c) <= (m * 2))
    {
        cout << "possible\n";
    }
    else
    {
        cout << "impossible\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}