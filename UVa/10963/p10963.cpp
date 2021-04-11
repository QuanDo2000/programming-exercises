#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = false;
int t, w, ny, sy, dif, ans, i;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> t;

    while (t--)
    {
        cin >> w;
        cin >> ny >> sy;
        w--;
        ans = 1;
        dif = ny - sy;
        if (DEBUG)
        {
            cout << w << "\n";
        }
        while (w--)
        {
            cin >> ny >> sy;
            if (dif != ny - sy)
            {
                ans = 0;
            }
        }
        if (ans == 1)
        {
            cout << "yes\n";
        }
        else
        {
            cout << "no\n";
        }
        if (t > 0)
        {
            cout << "\n";
        }
    }

    return 0;
}