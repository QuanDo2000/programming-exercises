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

int a[MAX_N];

void solve() {
  fill(a, a + MAX_N, 0);

  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  ll ans = 0;
  for (int i = 1; i < n; i++) {
    ans = max((ll)a[i] * a[i - 1], ans);
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