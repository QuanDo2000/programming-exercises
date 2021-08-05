#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int t;
ll n, a, b, m;
bool ans;

void solve()
{
    ans = 0;
    cin >> n >> a >> b;

    m = 1;
    while (m <= n)
    {
        if (((n - m) % b) == 0)
        {
            ans = 1;
            break;
        }
        m *= a;
        if (a == 1)
        {
            break;
        }
    }

    if (ans)
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