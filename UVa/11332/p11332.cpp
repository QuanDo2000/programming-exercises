#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int sum_digits(int n)
{
    int ans = 0;
    while (n)
    {
        ans += n % 10;
        n = n / 10;
    }
    return ans;
}

int rec(int n)
{
    if (n < 10 and n >= 0)
    {
        return n;
    }
    else
    {
        return rec(sum_digits(n));
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;

    while (cin >> n)
    {
        if (n == 0)
        {
            return 0;
        }
        int ans = rec(n);
        cout << ans << "\n";
    }

    return 0;
}