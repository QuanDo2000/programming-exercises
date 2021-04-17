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

    int tc, m, f;
    string pcs, pc;
    stringstream iss;

    cin >> tc;
    cin.ignore();
    while (tc--)
    {
        getline(cin, pcs);
        if (DEBUG)
        {
            cout << pcs;
        }
        iss.clear();
        iss.str(pcs);

        m = 0;
        f = 0;

        while (iss >> pc)
        {
            if (DEBUG)
            {
                cout << pc;
            }
            if (pc.compare("MF") == 0 || pc.compare("FM") == 0)
            {
                f++;
                m++;
            }
            else if (pc.compare("MM") == 0)
            {
                m += 2;
            }
            else if (pc.compare("FF") == 0)
            {
                f += 2;
            }
        }
        if (DEBUG)
        {
            cout << m << " " << f << "\n";
        }
        if (m == f && (m > 1))
        {
            cout << "LOOP\n";
        }
        else
        {
            cout << "NO LOOP\n";
        }
    }

    return 0;
}