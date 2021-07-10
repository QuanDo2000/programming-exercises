#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = 0;

char get_char(int c)
{
    return char(c + 96);
}

void solve()
{
    char s[28];
    cin >> s;

    if (DEBUG)
    {
        cout << s << " " << strlen(s) << "\n";
    }

    int l, r, c = 1;

    bool ans = 1;

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == get_char(c))
        {
            l = i - 1;
            r = i + 1;
            c++;
            break;
        }
    }
    if (c == 1)
    {
        ans = 0;
        l = -1;
        r = strlen(s);
    }

    while (l >= 0 || r < strlen(s))
    {
        if (DEBUG)
        {
            cout << c << " " << get_char(c) << " ";
            cout << l << " " << s[l] << " ";
            cout << r << " " << s[r] << "\n";
        }
        if (l >= 0 && get_char(c) == s[l])
        {
            l--;
            c++;
        }
        else if (r < strlen(s) && get_char(c) == s[r])
        {
            r++;
            c++;
        }
        else
        {
            ans = 0;
            break;
        }
    }

    if (ans)
    {
        cout << "YES"
             << "\n";
    }
    else
    {
        cout << "NO"
             << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }

    return 0;
}