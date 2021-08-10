#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using ii = pair<int, int>;
using vi = vector<int>;
using vii = vector<ii>;

const ll INF = INT_MAX;
const ll MOD = (ll)1 << 32;
const ld EPS = 1e-9;

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

ll factmod(ull n, ll p) {
  ll ans = 1;
  for (int i = 1; i <= n; i++) {
    ans = ((ans % p) * (i % p)) % p;
  }
  return ans;
}

void solve() {
  ull n;
  cin >> n;

  if (n > 33) {
    cout << 0 << "\n";
    return;
  }

  ll ans = factmod(n, MOD);
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