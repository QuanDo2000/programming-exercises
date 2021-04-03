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
        if (line.compare("#") == 0)
        {
            return 0;
        }
        else
        {
            cout << "Case " << i++ << ": ";
            if (line.compare("HELLO") == 0)
            {
                cout << "ENGLISH";
            }
            else if (line.compare("HOLA") == 0)
            {
                cout << "SPANISH";
            }
            else if (line.compare("HALLO") == 0)
            {
                cout << "GERMAN";
            }
            else if (line.compare("BONJOUR") == 0)
            {
                cout << "FRENCH";
            }
            else if (line.compare("CIAO") == 0)
            {
                cout << "ITALIAN";
            }
            else if (line.compare("ZDRAVSTVUJTE") == 0)
            {
                cout << "RUSSIAN";
            }
            else
            {
                cout << "UNKNOWN";
            }
            cout << "\n";
        }
    }

    return 0;
}