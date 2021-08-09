#include <bits/stdc++.h>
#include <regex>

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

string rep_special(string line)
{
    regex e("\\s[a-z][0-9]{2}\\s");
    return regex_replace(line, e, " *** ");
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;

    for (line; getline(cin, line);)
    {
        cout << rep_special(line) << "\n";
    }

    return 0;
}