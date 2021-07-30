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
  string s, t;
  cin >> s >> t;

  int ptr = t.size() - 1;
  int i = s.size() - 1;
  while (ptr >= 0 && i >= 0) {
    if (DEBUG) {
      cout << ptr << " " << i << "\n";
    }
    if (s[i] != t[ptr]) {
      i -= 2;
    } else {
      ptr--;
      i--;
    }
  }

  cout << (ptr < 0 ? "YES" : "NO") << "\n";
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