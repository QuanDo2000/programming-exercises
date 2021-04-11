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

    int a, b, ans;

    while (cin >> a >> b)
    {
        if (a == -1 && b == -1)
        {
            return 0;
        }
        if (a < b)
        {
            ans = min(b - a, a - b + 100);
        }
        else
        {
            ans = min(a - b, b - a + 100);
        }
        cout << ans << "\n";
    }

    return 0;
}