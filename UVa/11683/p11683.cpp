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

    int a, c, xi, ans, prev;

    while (cin >> a >> c)
    {
        if (a == 0 && c == 0)
        {
            return 0;
        }
        ans = 0;
        prev = a;
        for (int i = 0; i < c; i++)
        {
            cin >> xi;
            if (xi < prev)
            {
                ans += prev - xi;
            }
            prev = xi;
        }
        cout << ans << "\n";
    }

    return 0;
}