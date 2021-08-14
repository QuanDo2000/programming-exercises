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

const ll INF = 1000000;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 100000 + 2;

const bool DEBUG = 0;

void solve() {
  int k, r;
  cin >> k >> r;

  vi amount(k);
  for (int i = 0; i < k; i++) {
    cin >> amount[i];
  }
  int ans = 0;
  for (int i = 0; i < r; i++) {
    int mn = INF;
    for (int j = 0; j < k; j++) {
      int tmp;
      cin >> tmp;

      if (tmp != 0) {
        int sm = amount[j] / tmp;
        if (sm < mn) {
          mn = sm;
        }
      }
    }
    int rev;
    cin >> rev;
    rev *= mn;
    if (ans < rev) {
      ans = rev;
    }
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}