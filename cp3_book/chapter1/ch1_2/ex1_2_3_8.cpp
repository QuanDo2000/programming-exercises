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

const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

void subsetsUtil(vector<int> &arr, vector<vector<int>> &res, vector<int> &subset, int idx)
{
    res.push_back(subset);
    for (int i = idx; i < arr.size(); i++)
    {
        subset.push_back(arr[i]);
        subsetsUtil(arr, res, subset, i + 1);
        subset.pop_back();
    }
    return;
}

vector<vector<int>> subsets(vector<int> &arr)
{
    vector<int> subset;
    vector<vector<int>> res;

    int idx = 0;
    subsetsUtil(arr, res, subset, idx);

    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        arr.push_back(i);
    }

    vector<vector<int>> res = subsets(arr);

    for (int i = 0; i < res.size(); i++)
    {
        for (int j = 0; j < res[i].size(); j++)
        {
            cout << res[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}