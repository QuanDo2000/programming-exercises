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

    int t, n, prev, h, hi, lo, tc = 1;

    cin >> t;
    while (t--)
    {
        cin >> n;
        hi = 0;
        lo = 0;
        cin >> h;
        prev = h;
        for (int i = 0; i < n - 1; i++)
        {
            cin >> h;
            if (h > prev)
            {
                hi += 1;
            }
            else if (h < prev)
            {
                lo += 1;
            }
            prev = h;
        }
        cout << "Case " << tc++ << ": " << hi << " " << lo << "\n";
    }

    return 0;
}