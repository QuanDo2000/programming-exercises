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

const int MAX_N = 10 + 2;

const bool DEBUG = 0;

int a[MAX_N];

int onBit(int state, int pos) {
  return state | 1 << pos;
}

void solve() {
  fill(a, a + MAX_N, 1);
  int n, k;
  cin >> n >> k;

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < k; j++) {
      char ch;
      cin >> ch;
      if (ch == 'T') {
        a[i] = onBit(a[i], j);
      }
    }
  }
  int ans = 0;
  for (int state = 0; state < (1 << k); state++) {
    int mn = k;
    for (int i = 0; i < n; i++) {
      mn = min(mn, __builtin_popcount(a[i] ^ state));
    }
    ans = max(ans, mn);
  }
  cout << ans << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  solve();

  return 0;
}