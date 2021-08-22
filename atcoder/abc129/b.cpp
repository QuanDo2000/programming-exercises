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
  int n;
  cin >> n;

  vi w(n);
  for (int i = 0; i < n; i++) {
    cin >> w[i];
  }

  vi pre_sum(n), suf_sum(n);
  for (int i = 0; i < n; i++) {
    if (i == 0)
      pre_sum[i] = w[i];
    else
      pre_sum[i] = w[i] + pre_sum[i - 1];
  }
  for (int i = n - 1; i >= 0; i--) {
    if (i == n - 1)
      suf_sum[i] = w[i];
    else
      suf_sum[i] = w[i] + suf_sum[i + 1];
  }

  int mn = 1e4 + 2;
  for (int i = 0; i < n - 1; i++) {
    if (abs(pre_sum[i] - suf_sum[i + 1]) < mn)
      mn = abs(pre_sum[i] - suf_sum[i + 1]);
  }
  cout << mn << "\n";

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