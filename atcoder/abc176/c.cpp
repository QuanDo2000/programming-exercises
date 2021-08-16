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
  int n;
  cin >> n;

  vl a(n);
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }

  ll mx = 0, ans = 0;
  for (int i = 0; i < n; i++) {
    if (a[i] > mx)
      mx = a[i];
    else
      ans += mx - a[i];
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}