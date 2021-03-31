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

const int MAX_N = 1e6 + 1;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int v, n, l, h, ans, mid, i = 0;
    int *arr = (int *)malloc(MAX_N * sizeof(int));

    cin >> v;
    while (cin >> n)
    {
        arr[i] = n;
        i++;
    }

    l = 0;
    h = i;
    ans = -1;

    while (l <= h)
    {
        mid = (l + h) / 2;
        if (arr[mid] == v)
        {
            ans = mid;
            break;
        }
        else if (arr[mid] < v)
        {
            l = mid + 1;
        }
        else
        {
            h = mid - 1;
        }
    }
    cout << ans;

    free(arr);

    return 0;
}