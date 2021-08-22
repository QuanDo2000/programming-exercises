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

ld getDist(ii p1, ii p2) {
  ld xpow = pow(p1.first - p2.first, 2);
  ld ypow = pow(p1.second - p2.second, 2);
  return sqrt(xpow + ypow);
}

void solve() {
  int n;
  cin >> n;

  vii points(n);
  for (int i = 0; i < n; i++) {
    int x, y;
    cin >> x >> y;
    points[i] = {x, y};
  }

  // Each edge is used 2(n-1)! times
  // If the sum of all edges is sum, we have sum * 2(n-1)! / n! is the answer
  // Which is equal to sum * 2 / n

  ld ans = 0;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      ans += getDist(points[i], points[j]) * 2 / n;
    }
  }
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