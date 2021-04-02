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

int get_rot(int a, int b, int dir)
{
    if (a < b)
    {
        if (dir > 0)
        {
            return b - a;
        }
        else
        {
            return 40 - (b - a);
        }
    }
    else if (b < a)
    {
        if (dir > 0)
        {
            return 40 - (a - b);
        }
        else
        {
            return a - b;
        }
    }
    else
    {
        return 0;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int a, b, c, d, ans, rot1, rot2, rot3;

    while (cin >> a >> b >> c >> d)
    {
        if (a == 0 && b == 0 && c == 0 && d == 0)
        {
            return 0;
        }
        rot1 = get_rot(a, b, -1) * 360 / 40;
        rot2 = get_rot(b, c, 1) * 360 / 40;
        rot3 = get_rot(c, d, -1) * 360 / 40;
        ans = 360 * 2 + rot1 + 360 + rot2 + rot3;
        cout << ans << "\n";
    }

    return 0;
}