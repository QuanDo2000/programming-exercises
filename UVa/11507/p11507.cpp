#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

string rotate(string orig, string dir)
{
    if (dir.compare("+y") == 0)
    {
        if (orig.compare("+x") == 0)
        {
            return "+y";
        }
        else if (orig.compare("-x") == 0)
        {
            return "-y";
        }
        else if (orig.compare("+y") == 0)
        {
            return "-x";
        }
        else if (orig.compare("-y") == 0)
        {
            return "+x";
        }
        else if (orig.compare("+z") == 0 || orig.compare("-z") == 0)
        {
            return orig;
        }
    }
    else if (dir.compare("-y") == 0)
    {
        if (orig.compare("+x") == 0)
        {
            return "-y";
        }
        else if (orig.compare("-x") == 0)
        {
            return "+y";
        }
        else if (orig.compare("+y") == 0)
        {
            return "+x";
        }
        else if (orig.compare("-y") == 0)
        {
            return "-x";
        }
        else if (orig.compare("+z") == 0 || orig.compare("-z") == 0)
        {
            return orig;
        }
    }
    else if (dir.compare("+z") == 0)
    {
        if (orig.compare("+x") == 0)
        {
            return "+z";
        }
        else if (orig.compare("-x") == 0)
        {
            return "-z";
        }
        else if (orig.compare("+z") == 0)
        {
            return "-x";
        }
        else if (orig.compare("-z") == 0)
        {
            return "+x";
        }
        else if (orig.compare("+y") == 0 || orig.compare("-y") == 0)
        {
            return orig;
        }
    }
    else if (dir.compare("-z") == 0)
    {
        if (orig.compare("+x") == 0)
        {
            return "-z";
        }
        else if (orig.compare("-x") == 0)
        {
            return "+z";
        }
        else if (orig.compare("+z") == 0)
        {
            return "+x";
        }
        else if (orig.compare("-z") == 0)
        {
            return "-x";
        }
        else if (orig.compare("+y") == 0 || orig.compare("-y") == 0)
        {
            return orig;
        }
    }
    return orig;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int l;
    string dir, ans;

    while (cin >> l)
    {
        if (l == 0)
        {
            return 0;
        }
        ans = "+x";
        for (int i = 0; i < l - 1; i++)
        {
            cin >> dir;
            ans = rotate(ans, dir);
        }
        cout << ans << "\n";
    }

    return 0;
}