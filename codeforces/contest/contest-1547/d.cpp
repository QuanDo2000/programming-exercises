#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = 0;

const int MAX_N = 2 * 1e5;

void solve()
{
    int n;
    cin >> n;

    int x[MAX_N], y[MAX_N];
    memset(x, 0, sizeof(x));
    memset(y, 0, sizeof(y));

    for (int i = 0; i < n; i++)
    {
        cin >> x[i];
    }

    int prev;
    for (int i = 1; i < n; i++)
    {
        prev = x[i - 1] ^ y[i - 1];
        y[i] = prev & (prev ^ x[i]);
    }

    for (int i = 0; i < n; i++)
    {
        cout << y[i] << " ";
    }
    cout << "\n";
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