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

    int i = 1, n, x, ans;

    while (cin >> n)
    {
        if (n == 0)
        {
            return 0;
        }
        ans = 0;
        while (n--)
        {
            cin >> x;
            if (x > 0)
            {
                ans++;
            }
            else
            {
                ans--;
            }
        }
        cout << "Case " << i++ << ": " << ans << "\n";
    }

    return 0;
}