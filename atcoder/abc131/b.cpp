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

const int MAX_N = 300 + 2;

const bool DEBUG = 0;

void solve() {
  int n, l;
  cin >> n >> l;

  int mn = MAX_N, ans = 0;
  for (int i = 1; i <= n; i++) {
    ans += l + i - 1;
    if (abs(l + i - 1) < abs(mn)) mn = l + i - 1;
  }
  ans -= mn;
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