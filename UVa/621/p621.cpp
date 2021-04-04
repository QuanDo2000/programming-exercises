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

    string line;
    int t;

    cin >> t;
    while (t--)
    {
        cin >> line;
        if (line.compare("1") == 0 || line.compare("4") == 0 || line.compare("78") == 0)
        {
            cout << "+";
        }
        else if (line.substr(line.length() - 2, 2).compare("35") == 0)
        {
            cout << "-";
        }
        else if (line.at(0) == '9' && line.back() == '4')
        {
            cout << "*";
        }
        else
        {
            cout << "?";
        }
        cout << "\n";
    }

    return 0;
}