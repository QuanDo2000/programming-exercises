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
  int a, b, c, x, y;
  cin >> a >> b >> c >> x >> y;

  int ab = min(x, y);
  int ans = 0;
  if (a + b <= 2 * c)
    ans += (a + b) * ab;
  else
    ans += 2 * c * ab;

  int dif = x - y;
  if (dif > 0) {
    if (a <= 2 * c)
      ans += dif * a;
    else
      ans += dif * 2 * c;
  } else {
    if (b <= 2 * c)
      ans += -dif * b;
    else
      ans += -dif * 2 * c;
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