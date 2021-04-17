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

    int k, m, c, r, cid, count;
    unordered_set<int> courses;
    bool flag = true;

    while (cin >> k)
    {
        if (k == 0)
        {
            return 0;
        }
        cin >> m;

        courses.clear();
        flag = true;

        for (int i = 0; i < k; i++)
        {
            cin >> cid;
            courses.insert(cid);
        }
        for (int i = 0; i < m; i++)
        {
            cin >> c >> r;
            count = 0;
            for (int j = 0; j < c; j++)
            {
                cin >> cid;
                if (courses.count(cid) > 0)
                {
                    count++;
                }
            }
            if (count < r)
            {
                flag = false;
            }
        }
        if (flag)
        {
            cout << "yes";
        }
        else
        {
            cout << "no";
        }
        cout << "\n";
    }

    return 0;
}