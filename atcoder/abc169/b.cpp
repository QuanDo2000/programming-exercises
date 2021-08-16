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

  bool zero = 0;
  vl a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (a[i] == 0) zero = 1;
  }

  if (zero) {
    cout << 0 << "\n";
    return;
  }

  zero = 0;
  ll ans = 1;
  for (int i = 0; i < n; i++) {
    if (a[i] <= (ld)1e18 / ans)
      ans *= a[i];
    else {
      zero = 1;
      break;
    }
  }
  if (zero)
    cout << -1;
  else
    cout << ans;
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