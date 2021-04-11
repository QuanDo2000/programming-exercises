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

    int tc, n, num, p, diff;
    string ins;
    vector<int> vi;

    cin >> tc;
    while (tc--)
    {
        cin >> n;
        p = 0;
        vi.clear();
        for (int i = 0; i < n; i++)
        {
            cin >> ins;
            diff = 0;
            if (ins.compare("LEFT") == 0)
            {
                diff = -1;
            }
            else if (ins.compare("RIGHT") == 0)
            {
                diff = 1;
            }
            else
            {
                cin >> ins >> num;
                diff = vi.at(num - 1);
            }
            if (DEBUG)
            {
                cout << diff << " ";
            }
            vi.push_back(diff);
            p += diff;
        }
        cout << p << "\n";
    }

    return 0;
}