#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = double;

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

const bool DEBUG = false;
const vector<string> song = {"Happy", "birthday", "to", "you", "Rujia", "you"};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, i;
    string name;
    vector<string> vname;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> name;
        if (DEBUG)
        {
            cout << name << " ";
        }
        vname.push_back(name);
    }

    i = 0;
    while (i < vname.size() || i % 16 != 0)
    {
        string lyric;
        if (i % 16 == 15)
        {
            lyric = song.back();
        }
        else if (i % 16 == 11)
        {
            lyric = song.at(4);
        }
        else
        {
            lyric = song.at(i % 4);
        }
        cout << vname.at(i % vname.size()) << ": " << lyric << "\n";
        i++;
    }

    return 0;
}