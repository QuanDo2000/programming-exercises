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

const int MAX_N = 1e5 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

struct Birthday
{
    int day;
    int month;
    int year;
};

bool compare_birthdays(Birthday &a, Birthday &b)
{
    if (a.month < b.month)
        return true;
    else if (a.month > b.month)
        return false;
    else
    {
        if (a.day < b.day)
            return true;
        else if (a.day > b.day)
            return false;
        else
        {
            if (a.year > b.year)
                return true;
            else
                return false;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, d, m, y;
    list<Birthday> bdays;
    Birthday temp;

    cin >> n;

    while (n--)
    {
        cin >> d >> m >> y;
        temp.day = d;
        temp.month = m;
        temp.year = y;

        bdays.push_back(temp);
    }

    bdays.sort(compare_birthdays);

    for (auto bday : bdays)
    {
        cout << setw(2) << bday.day << " " << setw(2) << bday.month << " " << setw(4) << bday.year << "\n";
    }

    return 0;
}