#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using str = string;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;
using vvi = vector<vi>;
using vl = vector<ll>;
using vd = vector<ld>;
using vvd = vector<vd>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e5 + 2;

const bool DEBUG = 0;

void solve() {
  int n, m;
  cin >> n >> m;

  int mx = 0, mn = MAX_N;
  for (int i = 0; i < m; i++) {
    int l, r;
    cin >> l >> r;
    if (l > mx) mx = l;
    if (r < mn) mn = r;
  }
  int ans = mn - mx + 1;
  if (ans > 0)
    cout << ans;
  else
    cout << 0;
  cout << "\n";

  return;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  // int tc;
  // cin >> tc;
  // for (int i = 0; i < tc; i++)
  solve();

  return 0;
}