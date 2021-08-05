#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const int MAX_N = 102;

const bool DEBUG = 0;

void solve()
{
    int k, n, m;
    cin >> k >> n >> m;
    if (DEBUG)
    {
        cout << k << " " << n << " " << m << "\n";
    }

    int a[MAX_N], b[MAX_N];
    memset(a, 0, sizeof(a));
    memset(b, 0, sizeof(b));

    int ans[MAX_N * 2];
    memset(ans, 0, sizeof(ans));

    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        if (DEBUG)
        {
            cout << a[i] << " ";
        }
    }
    for (int i = 0; i < m; i++)
    {
        cin >> b[i];
        if (DEBUG)
        {
            cout << b[i] << " ";
        }
    }

    int i = 0, j = 0, pt = 0;
    while (i < n || j < m || pt < n + m)
    {
        if (DEBUG)
        {
            cout << "\n"
                 << i << "\n";
        }
        if (i < n && a[i] != 0 && a[i] <= k)
        {
            ans[pt] = a[i];
            i++;
            pt++;
        }
        else if (j < m && b[j] != 0 && b[j] <= k)
        {
            ans[pt] = b[j];
            j++;
            pt++;
        }
        else
        {
            if (i < n && a[i] == 0)
            {
                ans[pt] = a[i];
                i++;
                pt++;
                k++;
            }
            else if (j < m && b[j] == 0)
            {
                ans[pt] = b[j];
                j++;
                pt++;
                k++;
            }
            else
            {
                ans[0] = -1;
                break;
            }
        }
    }

    if (ans[0] == -1)
    {
        cout << -1 << "\n";
    }
    else
    {
        for (int i = 0; i < n + m; i++)
        {
            cout << ans[i] << " ";
        }
        cout << "\n";
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