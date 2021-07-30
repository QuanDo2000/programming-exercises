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

const int MAX_N = 1e5 + 2;

const bool DEBUG = 0;

int a[2][MAX_N];

void solve() {
  fill(&a[0][0], &a[0][0] + 2 * MAX_N, 0);

  int m;
  cin >> m;

  for (int i = 0; i < 2; i++) {
    for (int j = 1; j <= m; j++) {
      cin >> a[i][j];
      a[i][j] += a[i][j - 1];
    }
  }

  ll ans = INF;
  for (int i = 1; i <= m; i++) {
    int a0 = a[0][m] - a[0][i];
    int a1 = a[1][i - 1];
    if (DEBUG) {
      cout << a0 << " " << a1 << "\n";
    }
    int temp = max(a0, a1);
    ans = min(ans, (ll)temp);
  }
  cout << ans << "\n";
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