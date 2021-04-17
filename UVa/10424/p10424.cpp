#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int sum_one_digit(int val)
{
    if (val < 10)
    {
        return val;
    }
    int ans = 0;
    while (val != 0)
    {
        ans += val % 10;
        val /= 10;
    }
    return sum_one_digit(ans);
}

int get_str_sum(string name)
{
    int val, ans = 0;
    for (char &c : name)
    {
        val = int(c);
        if (val >= 65 && val <= 90)
        {
            ans += val - 64;
        }
        else if (val >= 97 && val <= 122)
        {
            ans += val - 96;
        }
    }

    return sum_one_digit(ans);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string name1, name2;
    int val1, val2;
    ld ans;

    while (getline(cin, name1))
    {
        getline(cin, name2);
        val1 = get_str_sum(name1);
        val2 = get_str_sum(name2);
        // cout << val1 << " " << val2 << "\n";

        if (val1 < val2)
        {
            ans = (ld)(val1) / val2 * 100.0;
        }
        else
        {
            ans = (ld)(val2) / val1 * 100.0;
        }

        cout << fixed << setprecision(2) << ans << " %\n";
    }

    return 0;
}