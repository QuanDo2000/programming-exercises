#include <bits/stdc++.h>

using namespace std;

// Shorthand for commonly used types
using ll = long long;
using ld = long double;
using vi = vector<int>;

const ll INF = INT_MAX;
const ll MOD = 1e9 + 7;
const ld EPS = 1e-9;

const int MAX_N = 1e3 + 2;

const bool DEBUG = 0;

void solve() {
  string s, t;
  cin >> s >> t;
  int n = s.size();
  int m = t.size();
  if (DEBUG) {
    cout << s << " " << t << "\n";
  }

  bool ans = false;
  for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
      if (DEBUG) {
        cout << i << " " << j << "\n";
      }
      int ptr = 0;
      bool ok = true;
      for (int k = i; k <= j; k++) {
        if (DEBUG) {
          cout << "\t" << k << " " << ptr << " " << ok << "\n";
        }
        if (ptr >= m) {
          break;
        }
        if (s[k] != t[ptr]) {
          ok = false;
          break;
        }
        ptr++;
      }
      for (int k = j - 1; k >= 0; k--) {
        if (DEBUG) {
          cout << "\t" << k << " " << ptr << " " << ok << "\n";
        }
        if (ptr >= m) {
          break;
        }
        if (s[k] != t[ptr]) {
          ok = false;
          break;
        }
        ptr++;
      }
      if (ok && ptr >= m) {
        ans = true;
        break;
      }
    }
    if (ans) {
      break;
    }
  }
  cout << (ans ? "YES" : "NO") << "\n";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int q;
  cin >> q;
  while (q--) {
    solve();
  }

  return 0;
}