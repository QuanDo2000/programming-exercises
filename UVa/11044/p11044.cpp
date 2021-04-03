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

    int t, a, b;
    cin >> t;

    while (t--)
    {
        cin >> a >> b;
        cout << int(ceil((a - 2) / 3.0) * ceil((b - 2) / 3.0)) << "\n";
    }

    return 0;
}