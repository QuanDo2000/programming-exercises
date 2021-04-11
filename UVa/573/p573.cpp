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
    cout << fixed;

    ld h, u, d, f, diff, curr;
    int day;
    bool flag;

    while (cin >> h >> u >> d >> f)
    {
        if (h == 0)
        {
            return 0;
        }
        curr = 0.0;
        day = 0;
        flag = false;
        diff = (ld)(u * f) / 100.0;
        while (curr <= h && curr >= 0)
        {
            day += 1;
            curr += u;
            u = max(0.0, u - diff);
            if (curr > h)
            {
                flag = true;
                break;
            }
            curr -= d;
        }
        if (flag)
        {
            cout << "success ";
        }
        else
        {
            cout << "failure ";
        }
        cout << "on day " << day << "\n";
    }

    return 0;
}