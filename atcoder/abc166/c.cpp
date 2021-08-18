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

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  int n, m;
  cin >> n >> m;

  vi good(n, 1);

  vl h(n);
  for (int i = 0; i < n; i++) {
    cin >> h[i];
  }

  for (int i = 0; i < m; i++) {
    int a, b;
    cin >> a >> b;
    if (h[a - 1] >= h[b - 1])
      good[b - 1] = 0;
    if (h[b - 1] >= h[a - 1])
      good[a - 1] = 0;
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    ans += good[i];
  }
  cout << ans << "\n";

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