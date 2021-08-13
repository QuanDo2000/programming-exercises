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
  int a, b, c, k;
  cin >> a >> b >> c >> k;

  int ans = 0;
  if (k >= a) {
    ans += a;
    k -= a;
  } else {
    ans += k;
    k -= k;
  }
  if (k >= b) {
    k -= b;
  } else {
    k -= k;
  }
  if (k > 0) {
    ans -= k;
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}