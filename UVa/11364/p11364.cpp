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

    int t, n, x, mi, mx;

    cin >> t;

    while (t--)
    {
        cin >> n;

        mi = 99;
        mx = 0;
        while (n--)
        {
            cin >> x;
            if (x > mx)
            {
                mx = x;
            }
            if (x < mi)
            {
                mi = x;
            }
        }
        cout << (mx - mi) * 2 << "\n";
    }

    return 0;
}