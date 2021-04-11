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

    int tc, x, a, b;
    bool dec, flag;

    cout << "Lumberjacks:\n";
    cin >> tc;
    while (tc--)
    {
        flag = true;
        cin >> a >> b;
        x = b - a;
        if (x > 0)
        {
            dec = false;
        }
        else
        {
            dec = true;
        }

        for (int i = 0; i < 8; i++)
        {
            a = b;
            cin >> b;
            x = b - a;
            if ((dec && (x > 0)) || (!dec && (x < 0)))
            {
                flag = false;
            }
        }
        if (flag)
        {
            cout << "Ordered\n";
        }
        else
        {
            cout << "Unordered\n";
        }
    }

    return 0;
}