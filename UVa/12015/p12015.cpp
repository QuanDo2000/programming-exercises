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

    int tc, t = 1, v, mx;
    string line;
    pair<string, int> pv;
    vector<pair<string, int>> vurl;

    cin >> tc;
    while (tc--)
    {
        cout << "Case #" << t++ << ":\n";
        mx = -1;
        vurl.clear();
        for (int i = 0; i < 10; i++)
        {
            cin >> line >> v;
            pv = make_pair(line, v);
            vurl.push_back(pv);
            if (v > mx)
            {
                mx = v;
            }
        }
        for (int i = 0; i < 10; i++)
        {
            pv = vurl.at(i);
            if (pv.second == mx)
            {
                cout << pv.first << "\n";
            }
        }
    }

    return 0;
}