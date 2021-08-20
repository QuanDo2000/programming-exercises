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

const int MAX_N = 2 * 1e5 + 2;

const bool DEBUG = 0;

void solve() {
  int n;
  cin >> n;

  vi a(n);
  int mx = 0, mx2 = 0;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (a[i] > mx) {
      if (mx > mx2) mx2 = mx;
      mx = a[i];
    } else if (a[i] > mx2)
      mx2 = a[i];
  }

  for (int i = 0; i < n; i++) {
    if (a[i] != mx)
      cout << mx;
    else
      cout << mx2;
    cout << "\n";
  }

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