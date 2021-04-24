#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = false;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int p, count, recv;
    string ci;
    char val;
    list<string> pl[2], heap;

    while (true)
    {
        p = 0;
        pl[0].clear();
        pl[1].clear();
        heap.clear();
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 13; j++)
            {
                cin >> ci;
                if (ci.compare("#") == 0)
                {
                    return 0;
                }
                pl[p].push_back(ci);
                p = (p + 1) % 2;
            }
        }

        p = 0;
        count = 1;
        recv = -1;
        while (pl[p].size() > 0)
        {
            ci = pl[p].back();
            pl[p].pop_back();

            heap.push_front(ci);

            count--;

            val = ci.back();
            switch (val)
            {
            case 'J':
                count = 1;
                recv = p;
                p = (p + 1) % 2;
                break;

            case 'Q':
                count = 2;
                recv = p;
                p = (p + 1) % 2;
                break;

            case 'K':
                count = 3;
                recv = p;
                p = (p + 1) % 2;
                break;

            case 'A':
                count = 4;
                recv = p;
                p = (p + 1) % 2;
                break;

            default:
                break;
            }

            if (count == 0)
            {
                p = (p + 1) % 2;
                count = 1;
                if (recv != -1)
                {
                    pl[recv].splice(pl[recv].begin(), heap);
                    recv = -1;
                }
            }
            if (DEBUG)
            {
                cout << ci << "\n";
            }
        }
        if (pl[0].size() > 0)
        {
            cout << "2" << setw(3) << pl[0].size();
        }
        else
        {
            cout << "1" << setw(3) << pl[1].size();
        }
        cout << "\n";
    }

    return 0;
}