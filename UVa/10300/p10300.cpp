#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int t, f, s, a, e, ans;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;
    while (t--)
    {
        cin >> f;
        ans = 0;
        while (f--)
        {
            cin >> s >> a >> e;
            ans += s * e;
        }
        cout << ans << "\n";
    }

    return 0;
}