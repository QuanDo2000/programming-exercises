#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, p, r, t = 1, i, j, mx;
    ld d, mi;
    string req, pro, reqi, ans;

    while (cin >> n >> p)
    {
        if (DEBUG)
        {
            cout << n << " " << p << "\n";
        }
        if (n == 0 && p == 0)
        {
            return 0;
        }
        else if (t != 1)
        {
            cout << "\n";
        }

        ans = "";
        mx = 0;
        mi = INF;

        cin.ignore();
        for (i = 0; i < n; i++)
        {
            getline(cin, req);
            if (DEBUG)
            {
                cout << req << "\n";
            }
        }
        for (i = 0; i < p; i++)
        {
            getline(cin, pro);
            cin >> d >> r;

            if (DEBUG)
            {
                cout << pro << "\n";
                cout << d << " " << r << "\n";
            }

            cin.ignore();
            for (j = 0; j < r; j++)
            {
                getline(cin, reqi);
            }
            if (r > mx || ans.compare("") == 0)
            {
                ans = pro;
                mx = r;
                mi = d;
            }
            else if (r == mx && d < mi)
            {
                ans = pro;
                mx = r;
                mi = d;
            }
        }
        cout << "RFP #" << t++ << "\n";
        cout << ans << "\n";
    }

    return 0;
}