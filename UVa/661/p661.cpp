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

    int n, m, c, ci, i, curr_p, mx, di, t = 1;
    vector<int> vc;
    vector<int> vstate;

    while (cin >> n >> m >> c)
    {
        if (n == 0 && m == 0 && c == 0)
        {
            return 0;
        }
        vc.clear();
        vstate.clear();
        curr_p = 0;
        mx = 0;
        for (i = 0; i < n; i++)
        {
            cin >> ci;
            vc.push_back(ci);
            vstate.push_back(0);
        }
        for (i = 0; i < m; i++)
        {
            cin >> di;
            if (vstate.at(di - 1) == 0)
            {
                vstate.at(di - 1) = 1;
                curr_p += vc.at(di - 1);
            }
            else
            {
                vstate.at(di - 1) = 0;
                curr_p -= vc.at(di - 1);
            }
            if (curr_p > mx)
            {
                mx = curr_p;
            }
        }
        cout << "Sequence " << t++ << "\n";
        if (mx > c)
        {
            cout << "Fuse was blown.\n";
        }
        else
        {
            cout << "Fuse was not blown.\n";
            cout << "Maximal power consumption was " << mx << " amperes.\n";
        }
        cout << "\n";
    }

    return 0;
}