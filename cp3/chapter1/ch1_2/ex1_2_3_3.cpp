#include <bits/stdc++.h>

using namespace std;

bool DEBUG = false;

string weekdays[7] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
string months[12] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};
int t[] = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};

int d, m, y, date;
char mstr[50];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> d >> mstr >> y;

    if (DEBUG)
        cout << d << " " << mstr << " " << y << "\n";

    m = 0;
    while (m < 12)
    {
        m++;
        if (months[m - 1].compare(mstr) == 0)
            break;
    }
    if (DEBUG)
        cout << d << " " << m << " " << y << "\n";

    y -= m < 3;
    date = (y + y / 4 - y / 100 + y / 400 + t[m - 1] + d) % 7;
    cout << weekdays[date];

    return 0;
}