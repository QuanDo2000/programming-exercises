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
  ll n, m, t;
  cin >> n >> m >> t;

  ll cap = n;

  int a = 0, b = 0, prev = 0;
  for (int i = 0; i < m; i++) {
    cin >> a >> b;
    n -= a - prev;
    if (n <= 0) {
      cout << "No\n";
      return;
    }
    n += b - a;
    n = min(cap, n);
    prev = b;
  }
  n -= t - prev;
  if (n <= 0)
    cout << "No\n";
  else
    cout << "Yes\n";

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