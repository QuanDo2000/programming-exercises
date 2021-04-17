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

    int i, xi, prev;
    string num;

    while (cin >> num)
    {
        if (num.compare("END") == 0)
        {
            return 0;
        }
        i = 1;
        if (num.size() < 9)
        {
            prev = stoi(num);
        }
        else
        {
            prev = INF;
        }
        xi = num.size();
        num = to_string(xi);

        while (prev != xi)
        {
            prev = xi;
            xi = num.size();
            num = to_string(xi);
            i++;
        }
        cout << i << "\n";
    }

    return 0;
}