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

    int t, num, bal;
    string op;

    cin >> t;
    bal = 0;
    while (t--)
    {
        cin >> op;
        if (op.compare("donate") == 0)
        {
            cin >> num;
            bal += num;
        }
        else if (op.compare("report") == 0)
        {
            cout << bal << "\n";
        }
    }

    return 0;
}