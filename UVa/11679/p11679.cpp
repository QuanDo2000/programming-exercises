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

    int b, n, r, c, d, v;
    bool flag = true;
    vector<int> vb;

    while (cin >> b >> n)
    {
        if (b == 0 && n == 0)
        {
            return 0;
        }
        vb.clear();
        for (int i = 0; i < b; i++)
        {
            cin >> r;
            vb.push_back(r);
        }
        for (int i = 0; i < n; i++)
        {
            cin >> d >> c >> v;
            vb.at(d - 1) -= v;
            vb.at(c - 1) += v;
        }
        flag = true;
        for (int i = 0; i < b; i++)
        {
            if (vb.at(i) < 0)
            {
                flag = false;
            }
        }
        if (flag)
        {
            cout << "S\n";
        }
        else
        {
            cout << "N\n";
        }
    }

    return 0;
}