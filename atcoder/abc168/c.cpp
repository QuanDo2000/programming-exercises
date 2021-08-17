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

const ld PI = M_PI;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  int a, b, h, m;
  cin >> a >> b >> h >> m;

  ld hh = (30 * (h % 12) + (ld)m * 0.5) * PI / 180;
  ld mh = ((ld)m * 6) * PI / 180;

  if (DEBUG) cout << hh << " " << mh << "\n";

  ld mn = abs(hh - mh);
  if (2 * PI - mn < mn) mn = 2 * PI - mn;

  ld ans = sqrt(a * a + b * b - 2 * a * b * cos(mn));
  cout << fixed << setprecision(9) << ans << "\n";

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