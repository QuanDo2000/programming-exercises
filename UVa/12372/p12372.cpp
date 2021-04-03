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

    int t, l, w, h, i = 1;

    cin >> t;
    while (t--)
    {
        cin >> l >> w >> h;
        cout << "Case " << i++ << ": ";
        if (l > 20 || w > 20 || h > 20)
        {
            cout << "bad";
        }
        else
        {
            cout << "good";
        }
        cout << "\n";
    }

    return 0;
}