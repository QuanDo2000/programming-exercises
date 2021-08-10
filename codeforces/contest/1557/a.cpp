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

void solve() {
  int n;
  cin >> n;

  ll mx = -INF;
  ll sum = 0;
  for (int i = 0; i < n; i++) {
    ll temp;
    cin >> temp;
    if (temp > mx) {
      mx = temp;
    }
    sum += temp;
  }

  ld ans = (ld)(sum - mx) / (n - 1) + mx;
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