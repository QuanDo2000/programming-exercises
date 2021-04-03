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

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, a, b, c;
    vector<int> nums;

    cin >> t;

    for (int i = 1; i <= t; i++)
    {
        cin >> a >> b >> c;
        nums.clear();
        nums.push_back(a);
        nums.push_back(b);
        nums.push_back(c);
        sort(nums.begin(), nums.end());
        cout << "Case " << i << ": " << nums.at(1) << "\n";
    }

    return 0;
}