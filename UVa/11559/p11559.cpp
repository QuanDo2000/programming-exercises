#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, b, h, w, p, a, ans, cost;

    while (cin >> n)
    {
        cin >> b >> h >> w;
        if (DEBUG)
        {
            cout << n << " " << b << " " << h << " " << w;
        }
        ans = INF;
        cost = 0;
        while (h--)
        {
            cin >> p;
            for (int i = 0; i < w; i++)
            {
                cin >> a;
                if (a >= n)
                {
                    cost = p * n;
                    if (cost < ans)
                    {
                        ans = cost;
                    }
                }
            }
        }
        if (ans <= b)
        {
            cout << ans;
        }
        else
        {
            cout << "stay home";
        }
        cout << "\n";
    }

    return 0;
}