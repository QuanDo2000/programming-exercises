#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using vi = vector<int>;
using vvi = vector<vi>;
using ii = pair<int, int>;
using vii = vector<ii>;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int k, n, m, x, y, dx, dy;

    while (cin >> k)
    {
        if (k == 0)
        {
            return 0;
        }
        cin >> n >> m;
        while (k--)
        {
            cin >> x >> y;
            dx = x - n;
            dy = y - m;
            if (dx == 0 || dy == 0)
            {
                cout << "divisa";
            }
            else if (dx > 0 && dy > 0)
            {
                cout << "NE";
            }
            else if (dx > 0 && dy < 0)
            {
                cout << "SE";
            }
            else if (dx < 0 && dy > 0)
            {
                cout << "NO";
            }
            else
            {
                cout << "SO";
            }
            cout << "\n";
        }
    }

    return 0;
}