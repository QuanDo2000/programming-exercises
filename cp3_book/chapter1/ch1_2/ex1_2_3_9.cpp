#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using vi = vector<int>;
using vvi = vector<vi>;
using ii = pair<int, int>;
using vii = vector<ii>;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int todec(int base, string num)
{
    int ans = 0;
    for (int i = 0; i < num.size(); i++)
    {
        ans += (int(num[i]) - int('A') + 10) * pow(base, num.size() - i - 1);
    }
    return ans;
}

string tobase(int base, int num)
{
    string ans = "";
    while (num > 0)
    {
        ans = to_string(num % base) + ans;
        num /= base;
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string num;
    int x, y, n;

    cin >> x >> num >> y;

    if (x != 10)
    {
        n = todec(x, num);
    }

    cout << tobase(y, n);

    return 0;
}