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

    int p, s, numr, gift, t = 1;
    string name, recv, line;
    stringstream iss;
    vector<string> vname;
    unordered_map<string, int> mname;

    while (cin >> p)
    {
        if (t > 1)
            cout << "\n";
        vname.clear();
        mname.clear();
        for (int i = 0; i < p; i++)
        {
            cin >> name;
            vname.push_back(name);
            mname.insert({name, 0});
        }

        for (int i = 0; i < p; i++)
        {
            cin >> name >> s >> numr;

            if (numr == 0)
                continue;
            gift = s / numr;
            mname.at(name) -= gift * numr;

            for (int j = 0; j < numr; j++)
            {
                cin >> recv;
                mname.at(recv) += gift;
            }
        }

        for (int i = 0; i < p; i++)
        {
            cout << vname.at(i) << " " << mname.at(vname.at(i)) << "\n";
        }
        t++;
    }

    return 0;
}