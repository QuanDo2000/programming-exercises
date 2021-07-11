#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;
using vi = vector<int>;

const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const bool DEBUG = 0;

const int MAX_N = 100 + 2;

void solve()
{
    int n;
    cin >> n;

    int a[MAX_N] = {}, b[MAX_N] = {};
    vi inc, dec;
    inc.clear();
    dec.clear();

    int sumA = 0, sumB = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        sumA += a[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> b[i];
        sumB += b[i];
    }

    if (sumA != sumB)
    {
        cout << "-1\n";
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (a[i] < b[i])
        {
            for (int j = 0; j < (b[i] - a[i]); j++)
            {
                inc.push_back(i + 1);
            }
        }
        else if (a[i] > b[i])
        {
            for (int j = 0; j < (a[i] - b[i]); j++)
            {
                dec.push_back(i + 1);
            }
        }
    }

    cout << inc.size() << "\n";
    for (int i = 0; i < inc.size(); i++)
    {
        cout << dec[i] << " " << inc[i] << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }

    return 0;
}