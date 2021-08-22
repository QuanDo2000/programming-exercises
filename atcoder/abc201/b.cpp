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

  int mx = 0, mx2 = 0;
  str ans = "", mx_name = "";
  for (int i = 0; i < n; i++) {
    str s;
    int t;
    cin >> s >> t;
    if (t > mx) {
      if (mx > mx2) {
        mx2 = mx;
        ans = mx_name;
      }
      mx = t;
      mx_name = s;
    } else if (t > mx2) {
      mx2 = t;
      ans = s;
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