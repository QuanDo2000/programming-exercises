#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int tc, t = 1, n, msum, jsum, d;

    cin >> tc;
    while (tc--)
    {
        cin >> n;
        msum = 0;
        jsum = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> d;
            msum += ((d / 30) + 1) * 10;
            jsum += ((d / 60) + 1) * 15;
        }
        cout << "Case " << t++ << ": ";
        if (msum < jsum)
        {
            cout << "Mile " << msum;
        }
        else if (jsum < msum)
        {
            cout << "Juice " << jsum;
        }
        else
        {
            cout << "Mile Juice " << msum;
        }
        cout << "\n";
    }

    return 0;
}