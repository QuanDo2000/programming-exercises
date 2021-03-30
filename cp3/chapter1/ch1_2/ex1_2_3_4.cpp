#include <bits/stdc++.h>

using namespace std;
int n;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // less to sort in increasing order
    // greater to sort in decreasing order
    set<int, less<int>> sm;
    set<int, less<int>>::iterator itr; // iterator for the set

    while (cin >> n)
    {
        sm.insert(n);
    }

    for (itr = sm.begin(); itr != sm.end(); itr++) // iterate through the set
    {
        cout << *itr << " "; // '*itr' to access element in the set
    }

    return 0;
}