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
    int i = 1;

    while (cin >> line)
    {
        if (line.compare("*") == 0)
        {
            return 0;
        }
        cout << "Case " << i++ << ": ";
        if (line.compare("Hajj") == 0)
        {
            cout << "Hajj-e-Akbar";
        }
        else if (line.compare("Umrah") == 0)
        {
            cout << "Hajj-e-Asghar";
        }
        cout << "\n";
    }

    return 0;
}