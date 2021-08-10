#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e5 + 2;

const bool DEBUG = 0;

int a[MAX_N], parent[MAX_N];

int Find(int x) {
  if (parent[x] != x) {
    parent[x] = Find(parent[x]);
  }
  return parent[x];
}

void Union(int x, int y) {
  int xset = Find(x);
  int yset = Find(y);

  if (xset == yset) {
    return;
  }

  parent[yset] = xset;
}

void solve() {
  fill(a, a + MAX_N, 0);
  fill(parent, parent + MAX_N, 0);

  int n, k;
  cin >> n >> k;

  vi val = {};

  for (int i = 0; i < n; i++) {
    cin >> a[i];
    val.push_back(a[i]);
    parent[i] = i;
  }

  sort(val.begin(), val.end());
  map<int, int> d;
  for (int i = 0; i < val.size(); i++) {
    d[val[i]] = i;
  }

  for (int i = 0; i < n; i++) {
    a[i] = d[a[i]];
  }

  for (int i = 1; i < n; i++) {
    if (a[i] == a[i - 1] + 1) {
      Union(i, i - 1);
    }
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (parent[i] == i) {
      ans++;
    }
  }
  if (DEBUG) {
    cout << ans << "\n";
  }
  cout << ((k < ans) ? "No" : "Yes") << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }

  return 0;
}