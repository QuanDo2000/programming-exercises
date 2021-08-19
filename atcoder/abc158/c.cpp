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
  int a, b;
  cin >> a >> b;

  ld lo_a = a / 0.08, hi_a = (a + 1) / 0.08;
  ld lo_b = b / 0.1, hi_b = (b + 1) / 0.1;

  for (int i = ceil(lo_a); i < hi_a; i++) {
    if (i < hi_b && i >= lo_b) {
      cout << i << "\n";
      return;
    }
  }
  cout << -1 << "\n";

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