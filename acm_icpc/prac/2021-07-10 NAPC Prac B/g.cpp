#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const bool DEBUG = 0;

void solve()
{
    map<string, string> d = {};
    string s;

    bool mess = 0;

    while (getline(cin, s))
    {
        if (DEBUG)
        {
            cout << s << "\n";
        }
        stringstream iss(s);
        string k, i;
        if (s == "")
        {
            mess = 1;
            continue;
        }
        if (mess)
        {
            iss >> k;
            map<string, string>::iterator it;
            it = d.find(k);
            if (DEBUG)
            {
                cout << k << "\n";
            }
            if (it != d.end())
            {
                cout << it->second << "\n";
            }
            else
            {
                cout << "eh\n";
            }
        }
        else
        {
            iss >> i >> k;
            if (DEBUG)
            {
                cout << k << " " << i << "\n";
            }
            d[k] = i;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}