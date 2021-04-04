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
const int MAX_N = 1e2 + 1;

const bool DEBUG = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.precision(4);
    cout << fixed;

    int ms, m, n, i;
    ld d, l, r, val, owe;
    ld rs[MAX_N];

    while (true)
    {
        cin >> ms >> d >> l >> n;
        fill(rs, rs + MAX_N, 0);

        if (ms < 0)
        {
            return 0;
        }

        while (n--)
        {
            cin >> m >> r;
            rs[m] = r;
        }
        val = d + l;
        owe = l;

        if (DEBUG)
        {
            cout << ms << " " << d << " " << l << "\n";
            cout << val << " " << owe << "\n";
        }

        for (i = 0; i <= ms; i++)
        {
            if (rs[i] != 0)
            {
                r = rs[i];
            }
            val *= 1 - r;
            if (i != 0)
            {
                owe -= l / ms;
            }
            if (val >= owe)
            {
                break;
            }
        }
        cout << i << " month";
        if (i != 1)
        {
            cout << "s";
        }
        cout << "\n";
    }

    return 0;
}