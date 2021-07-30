#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  int W, H;
  cin >> W >> H;
  int x1, y1, x2, y2;
  cin >> x1 >> y1 >> x2 >> y2;
  int w, h;
  cin >> w >> h;

  if (x2 - x1 + w > W && y2 - y1 + h > H) {
    cout << "-1\n";
    return;
  }

  ld ans = INF;
  if (x1 >= w || y1 >= h || W - x2 >= w || H - y2 >= h) {
    ans = min(ans, (ld)0);
  }
  if (y2 + h - y1 <= H && h >= y1) {
    ans = min(ans, (ld)h - y1);
  }
  if (x2 + w - x1 <= W && w >= x1) {
    ans = min(ans, (ld)w - x1);
  }
  if (y1 - (h - (H - y2)) >= 0 && h >= H - y2) {
    ans = min(ans, (ld)h - (H - y2));
  }
  if (x1 - (w - (W - x2)) >= 0 && w >= W - x2) {
    ans = min(ans, (ld)w - (W - x2));
  }
  cout << fixed << setprecision(9) << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tc;
  cin >> tc;
  while (tc--) {
    solve();
  }

  return 0;
}