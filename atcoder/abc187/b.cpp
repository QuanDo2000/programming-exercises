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

bool check(ii p1, ii p2) {
  int ydiff = p2.second - p1.second;
  int xdiff = p2.first - p1.first;
  ld slope = (ld)ydiff / xdiff;

  if (DEBUG) cout << slope << "\n";

  if (slope >= -1 - EPS && slope <= 1 + EPS) {
    return true;
  }
  return false;
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

  int ans = 0;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (check(points[i], points[j])) ans++;
    }
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