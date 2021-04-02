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

    char c;
    int s = 1;

    while (cin.get(c))
    {
        if (c == '"')
        {
            if (s == 1)
            {
                cout << "``";
                s *= -1;
            }
            else
            {
                cout << "''";
                s *= -1;
            }
        }
        else
        {
            cout << c;
        }
    }

    return 0;
}