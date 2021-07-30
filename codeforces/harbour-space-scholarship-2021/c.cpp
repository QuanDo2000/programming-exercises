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

const int MAX_N = 1e9 + 2;

const bool DEBUG = 0;

void solve() {
  string s;
  cin >> s;

  int ans = 9;
  int cnt0 = 0, cnt1 = 0;
  for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
      cnt0 += s[i] != '0';
    } else {
      cnt1 += s[i] == '1';
    }
    if (cnt0 > cnt1 + (10 - i) / 2 || cnt1 > cnt0 + (9 - i) / 2) {
      ans = min(ans, i);
    }
  }
  cnt0 = cnt1 = 0;
  for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
      cnt0 += s[i] == '1';
    } else {
      cnt1 += s[i] != '0';
    }
    if (cnt0 > cnt1 + (10 - i) / 2 || cnt1 > cnt0 + (9 - i) / 2) {
      ans = min(ans, i);
    }
  }
  cout << ans + 1 << "\n";
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