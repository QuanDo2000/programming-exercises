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

  vi vac(4, 0), con(4, 0);
  for (int i = 0; i < n; i++) {
    str par;
    cin >> par;
    if (par[0] == 'Y') {
      vac[0]++;
      for (int j = 1; j < 4; j++) {
        if (par[j] == 'Y') {
          vac[j]++;
        }
      }
    } else if (par[0] != 'Y') {
      con[0]++;
      for (int j = 1; j < 4; j++) {
        if (par[j] == 'Y') {
          con[j]++;
        }
      }
    }
  }
  for (int i = 1; i < 4; i++) {
    ld v = (ld)vac[i] / vac[0];
    ld c = (ld)con[i] / con[0];
    if (v >= c) {
      cout << "Not Effective";
    } else {
      cout << fixed << setprecision(6) << (1 - v / c) * 100;
    }
    cout << "\n";
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}